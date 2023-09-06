from .mixins import PropertyMixin


class Linedef(PropertyMixin):
    def __init__(self, id=None, v1=None, v2=None, blocking=None, blockmonsters=None, twosided=None, dontpegtop=None, dontpegbottom=None, secret=None, blocksound=None, dontdraw=None, mapped=None, passuse=None, translucent=None, jumpover=None, blockfloaters=None, playercross=None, playeruse=None, monstercross=None, monsteruse=None, impact=None, playerpush=None, monsterpush=None, missilecross=None, repeatspecial=None, special=None, arg0=None, arg1=None, arg2=None, arg3=None, arg4=None, sidefront=None, sideback=None, comment=None, alpha=None, renderstyle=None, anycross=None, monsteractivate=None, blockplayers=None, blockeverything=None, firstsideonly=None, zoneboundary=None, clipmidtex=None, wrapmidtex=None, midtex3d=None, midtex3dimpassible=None, checkswitchrange=None, blockprojectiles=None, blockuse=None, blocksight=None, blockhitscan=None, locknumber=None, arg0str=None, moreids=None, transparent=None, automapstyle=None, revealed=None, noskywalls=None, drawfullheight=None, health=None, healthgroup=None, damagespecial=None, deathspecial=None):
        self.id = id
        self.v1 = v1
        self.v2 = v2
        self.blocking = blocking
        self.blockmonsters = blockmonsters
        self.twosided = twosided
        self.dontpegtop = dontpegtop
        self.dontpegbottom = dontpegbottom
        self.secret = secret
        self.blocksound = blocksound
        self.dontdraw = dontdraw
        self.mapped = mapped
        self.passuse = passuse
        self.translucent = translucent
        self.jumpover = jumpover
        self.blockfloaters = blockfloaters
        self.playercross = playercross
        self.playeruse = playeruse
        self.monstercross = monstercross
        self.monsteruse = monsteruse
        self.impact = impact
        self.playerpush = playerpush
        self.monsterpush = monsterpush
        self.missilecross = missilecross
        self.repeatspecial = repeatspecial
        self.special = special
        self.arg0 = arg0
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.sidefront = sidefront
        self.sideback = sideback
        self.comment = comment
        self.alpha = alpha
        self.renderstyle = renderstyle
        self.anycross = anycross
        self.monsteractivate = monsteractivate
        self.blockplayers = blockplayers
        self.blockeverything = blockeverything
        self.firstsideonly = firstsideonly
        self.zoneboundary = zoneboundary
        self.clipmidtex = clipmidtex
        self.wrapmidtex = wrapmidtex
        self.midtex3d = midtex3d
        self.midtex3dimpassible = midtex3dimpassible
        self.checkswitchrange = checkswitchrange
        self.blockprojectiles = blockprojectiles
        self.blockuse = blockuse
        self.blocksight = blocksight
        self.blockhitscan = blockhitscan
        self.locknumber = locknumber
        self.arg0str = arg0str
        self.moreids = moreids
        self.transparent = transparent
        self.automapstyle = automapstyle
        self.revealed = revealed
        self.noskywalls = noskywalls
        self.drawfullheight = drawfullheight
        self.health = health
        self.healthgroup = healthgroup
        self.damagespecial = damagespecial
        self.deathspecial = deathspecial
        super().__init__(kwargs={
            'id': self.id, 'v1': self.v1, 'v2': self.v2, 'blocking': self.blocking, 'blockmonsters': self.blockmonsters, 'twosided': self.twosided, 'dontpegtop': self.dontpegtop, 'dontpegbottom': self.dontpegbottom, 'secret': self.secret, 'blocksound': self.blocksound, 'dontdraw': self.dontdraw, 'mapped': self.mapped, 'passuse': self.passuse, 'translucent': self.translucent, 'jumpover': self.jumpover, 'blockfloaters': self.blockfloaters, 'playercross': self.playercross, 'playeruse': self.playeruse, 'monstercross': self.monstercross, 'monsteruse': self.monsteruse, 'impact': self.impact, 'playerpush': self.playerpush, 'monsterpush': self.monsterpush, 'missilecross': self.missilecross, 'repeatspecial': self.repeatspecial, 'special': self.special, 'arg0': self.arg0, 'arg1': self.arg1, 'arg2': self.arg2, 'arg3': self.arg3, 'arg4': self.arg4, 'sidefront': self.sidefront, 'sideback': self.sideback, 'comment': self.comment, 'alpha': self.alpha, 'renderstyle': self.renderstyle, 'anycross': self.anycross, 'monsteractivate': self.monsteractivate, 'blockplayers': self.blockplayers, 'blockeverything': self.blockeverything, 'firstsideonly': self.firstsideonly, 'zoneboundary': self.zoneboundary, 'clipmidtex': self.clipmidtex, 'wrapmidtex': self.wrapmidtex, 'midtex3d': self.midtex3d, 'midtex3dimpassible': self.midtex3dimpassible, 'checkswitchrange': self.checkswitchrange, 'blockprojectiles': self.blockprojectiles, 'blockuse': self.blockuse, 'blocksight': self.blocksight, 'blockhitscan': self.blockhitscan, 'locknumber': self.locknumber, 'arg0str': self.arg0str, 'moreids': self.moreids, 'transparent': self.transparent, 'automapstyle': self.automapstyle, 'revealed': self.revealed, 'noskywalls': self.noskywalls, 'drawfullheight': self.drawfullheight, 'health': self.health, 'healthgroup': self.healthgroup, 'damagespecial': self.damagespecial, 'deathspecial': self.deathspecial
        })
        