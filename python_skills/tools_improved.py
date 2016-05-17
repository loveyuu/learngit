# encoding=utf-8
"""
2016/5/17
导表工具
由于表的问题以及个人原因, 忙活了大半天
还要继续修改, 代码乱的一塌糊涂...

2016/5/18
基于多进程,由于此类型计算属于cpu密集型
参考：https://segmentfault.com/a/1190000000414339#articleHeader5
性能提高了很多很多
"""
import sys
reload(sys)

sys.setdefaultencoding('utf8')
import xlrd
import os
import shutil
from multiprocessing import Pool
import time


def do(t, v):
    if t == "0":
        if type(v) == str:
            v = 0
        return str(int(v))
    else:
        if type(v) == float:
            v = int(v)
        return '"%s"' % v


def hang(f):
    f_name = f.replace(
        '.', '_')[:-5] if f.endswith('.xlsx') else f.replace('.', '_')[:-4]
    record_name = 'record_' + f_name
    print "now loading {0}...wait for a moment".format(f)
    data = xlrd.open_workbook(f)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    da = open('lua\\'+f_name+'.lua', 'w+')
    da.write(
        "---@classdef %s\nlocal %s = {}\n\n" % (record_name, record_name))
    default_value, attr_desc = [], []

    for v in table.row_values(1):
        dv = "0" if v == 'int' else '""'
        default_value.append(dv)

    for v in table.row_values(2):
        attr_desc.append(v)

    for v, d, attr in zip(table.row_values(4), default_value, attr_desc):
        da.write("%s.%s = %s --%s\n" % (record_name, v, d, attr))

    da.write("%s = {\n   _data = {\n    " % (f_name))
    id_index = {}
    for i in xrange(5, nrows):
        row_data = table.row_values(i)
        exs = "{"+','.join([do(t, v)
                            for t, v in zip(default_value, row_data)])+",},"
        da.write("[%d] = %s\n    " %
                 (i-4, exs))
        print exs

        id_index[str(int(row_data[0]))] = i-4
    da.write("}\n}\n\n")

    ids = table.col_values(0)[5:]
    _ids = [str(int(i)) for i in ids]
    _ids.sort()

    da.write("local __index_id = {\n    ")
    for i in _ids:
        da.write("[%s] = %s,\n    " % (i, id_index[i]))
    da.write("\n}\n")

    da.write("local __key_map = {\n    ")
    for i in xrange(0, ncols):
        da.write("%s = %d,\n    " % (table.col_values(i)[4], i+1))
    da.write("\n}\n")

    da.write(
        """
local m = {
    __index = function(t, k)
        if k == "toObject" then
            return function()
                local o = {}
                for key, v in pairs (__key_map) do
                    o[key] = t._raw[v]
                end
                return o
            end
        end

        assert(__key_map[k], "cannot find " .. k .. " in %s")


        return t._raw[__key_map[k]]
    end
}\n\n
    """ % (record_name,)
    )

    da.write(
        """
function %s.getLength()
    return #%s._data
end\n\n
    """ % (f_name, f_name)
    )

    da.write(
        """
function %s.hasKey(k)
    if __key_map[k] == nil then
        return false
    else
        return true
    end
end\n\n
    """ % (f_name)
    )

    da.write(
        """
---
--@return @class %s
function %s.indexOf(index)
    if index == nil then
        return nil
    end

    return setmetatable({_raw = %s._data[index]}, m)

end\n\n
    """ % (record_name, f_name, f_name)
    )
    da.write(
        """
---
--@return @class %s
function %s.get(id)

    return %s.indexOf(__index_id[id])

end\n\n
    """ % (record_name, f_name, f_name)
    )
    da.write(
        """
function %s.set(id, key, value)
    local record = %s.get(id)
    if record then
        local keyIndex = __key_map[key]
        if keyIndex then
            record._raw[keyIndex] = value
        end
    end
end\n\n
    """ % (f_name, f_name)
    )

    da.write(
        """
function %s.get_index_data()
    return __index_id
end\n\n
    """ % f_name
    )
    print "{0} is loaded".format(f)

if __name__ == '__main__':

    s = time.time()
    file_list = os.listdir(os.getcwd())
    handle_file_list = [
        i for i in file_list if i.endswith('.xlsx') or i.endswith('.xls')]

    if os.path.exists('lua'):
        shutil.rmtree('lua')
    os.mkdir('lua')

    pool = Pool()
    pool.map(hang, handle_file_list)
    pool.close()
    pool.join()
    print "all successfully!", time.time() - s
