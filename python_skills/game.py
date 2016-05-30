# encoding=utf-8
class PlayGame(object):
    def __init__(self, num=0):
        self.num = num


class WatchTV(object):
    def __init__(self, name=0):
        self.name = name


class BaseGameRole(object):
    def __init__(self, role_id, role_nickname, role_level, role_exp):
        self.role_id = role_id
        self.role_nickname = role_nickname
        self.role_level = role_level
        self.role_exp = role_exp

    def base_dumps(self):
        return self.role_id, self.role_nickname, self.role_level, self.role_exp

    def modify_role_exp(self, delta):
        if self.role_exp + delta:
            self.role_exp += delta
            return True


class GameRole(BaseGameRole):
    def __init__(self, *args, **kwargs):
        super(GameRole, self).__init__(*args, **kwargs)
        self.play_game = PlayGame(*kwargs.get('play_game', []))
        self.watch_tv = WatchTV(*kwargs.get('watch_tv', []))

    def dumps(self):
        return super(GameRole, self).base_dumps(), self.play_game, self.watch_tv


def calculate_attr(game_role_ob):
    """
    计算角色属性
    :param game_role_ob:
    :return:(num, name)
    """
    if not isinstance(game_role_ob, GameRole):
        raise Exception('game_role_ob is not target object')
    else:
        return game_role_ob.play_game.num, game_role_ob.watch_tv.name


if __name__ == "__main__":
    b = [10020, 'bestman', 30, 34000]
    d = {}
    a = GameRole(*b, **d)
    print a.role_exp
    print a.dumps()
    a.modify_role_exp(1000)
    print a.role_exp
    print calculate_attr(a)
    print calculate_attr.__doc__
