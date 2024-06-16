from .mixins import PropertyMixin


class Thing(PropertyMixin):
    def __init__(self, id=None, x=None, y=None, height=None, angle=None, type=None, skill1=None, skill2=None, skill3=None, skill4=None, skill5=None, ambush=None, single=None, dm=None, coop=None, friend=None, dormant=None, class1=None, class2=None, class3=None, standing=None, strifeally=None, translucent=None, invisible=None, special=None, arg0=None, arg1=None, arg2=None, arg3=None, arg4=None, comment=None, countsecret=None, arg0str=None, gravity=None, health=None, renderstyle=None, fillcolor=None, alpha=None, score=None, pitch=None, roll=None, scalex=None, scaley=None, scale=None, floatbobphase=None, flags=None, user_scriptname=None):
        self.id = id
        self.x = x
        self.y = y
        self.height = height
        self.angle = angle
        self.type = type
        self.skill1 = skill1
        self.skill2 = skill2
        self.skill3 = skill3
        self.skill4 = skill4
        self.skill5 = skill5
        self.ambush = ambush
        self.single = single
        self.dm = dm
        self.coop = coop
        self.friend = friend
        self.dormant = dormant
        self.class1 = class1
        self.class2 = class2
        self.class3 = class3
        self.standing = standing
        self.strifeally = strifeally
        self.translucent = translucent
        self.invisible = invisible
        self.special = special
        self.arg0 = arg0
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.comment = comment
        self.countsecret = countsecret
        self.arg0str = arg0str
        self.gravity = gravity
        self.health = health
        self.renderstyle = renderstyle
        self.fillcolor = fillcolor
        self.alpha = alpha
        self.score = score
        self.pitch = pitch
        self.roll = roll
        self.scalex = scalex
        self.scaley = scaley
        self.scale = scale
        self.floatbobphase = floatbobphase
        self.flags = flags
        self.user_scriptname = user_scriptname
        super().__init__(kwargs={
            'id': self.id, 'x': self.x, 'y': self.y, 'height': self.height, 'angle': self.angle, 'type': self.type, 'skill1': self.skill1, 'skill2': self.skill2, 'skill3': self.skill3, 'skill4': self.skill4, 'skill5': self.skill5, 'ambush': self.ambush, 'single': self.single, 'dm': self.dm, 'coop': self.coop, 'friend': self.friend, 'dormant': self.dormant, 'class1': self.class1, 'class2': self.class2, 'class3': self.class3, 'standing': self.standing, 'strifeally': self.strifeally, 'translucent': self.translucent, 'invisible': self.invisible, 'special': self.special, 'arg0': self.arg0, 'arg1': self.arg1, 'arg2': self.arg2, 'arg3': self.arg3, 'arg4': self.arg4, 'comment': self.comment, 'countsecret': self.countsecret, 'arg0str': self.arg0str, 'gravity': self.gravity, 'health': self.health, 'renderstyle': self.renderstyle, 'fillcolor': self.fillcolor, 'alpha': self.alpha, 'score': self.score, 'pitch': self.pitch, 'roll': self.roll, 'scalex': self.scalex, 'scaley': self.scaley, 'scale': self.scale, 'floatbobphase': self.floatbobphase, 'flags': self.flags, 'user_scriptname': self.user_scriptname
        })
        