from .mixins import PropertyMixin


class Sector(PropertyMixin):
    def __init__(self, heightfloor=None, heightceiling=None, texturefloor=None, textureceiling=None, lightlevel=None, special=None, id=None, comment=None, xpanningfloor=None, ypanningfloor=None, xpanningceiling=None, ypanningceiling=None, xscalefloor=None, yscalefloor=None, xscaleceiling=None, yscaleceiling=None, rotationfloor=None, rotationceiling=None, ceilingplane_a=None, ceilingplane_b=None, ceilingplane_c=None, ceilingplane_d=None, floorplane_a=None, floorplane_b=None, floorplane_c=None, floorplane_d=None, lightfloor=None, lightceiling=None, lightfloorabsolute=None, lightceilingabsolute=None, alphafloor=None, alphaceiling=None, renderstylefloor=None, renderstyleceiling=None, gravity=None, lightcolor=None, fadecolor=None, desaturation=None, silent=None, nofallingdamage=None, noattack=None, dropactors=None, norespawn=None, soundsequence=None, hidden=None, waterzone=None, moreids=None, damageamount=None, damagetype=None, damageinterval=None, leakiness=None, damageterraineffect=None, damagehazard=None, floorterrain=None, ceilingterrain=None, floor_reflect=None, ceiling_reflect=None, fogdensity=None, floorglowcolor=None, floorglowheight=None, ceilingglowcolor=None, ceilingglowheight=None, color_floor=None, color_ceiling=None, color_walltop=None, color_wallbottom=None, color_sprites=None, coloradd_floor=None, coloradd_ceiling=None, coloradd_sprites=None, coloradd_walls=None, colorization_floor=None, colorization_ceiling=None, noskywalls=None, portal_ceil_blocksound=None, portal_ceil_disabled=None, portal_ceil_nopass=None, portal_ceil_norender=None, portal_ceil_overlaytype=None, portal_floor_blocksound=None, portal_floor_disabled=None, portal_floor_nopass=None, portal_floor_norender=None, portal_floor_overlaytype=None, healthfloor=None, healthfloorgroup=None, healthceiling=None, healthceilinggroup=None, lm_sampledist_floor=None, lm_sampledist_ceiling=None, lm_dynamic=None):
        self.heightfloor = heightfloor
        self.heightceiling = heightceiling
        self.texturefloor = texturefloor
        self.textureceiling = textureceiling
        self.lightlevel = lightlevel
        self.special = special
        self.id = id
        self.comment = comment
        self.xpanningfloor = xpanningfloor
        self.ypanningfloor = ypanningfloor
        self.xpanningceiling = xpanningceiling
        self.ypanningceiling = ypanningceiling
        self.xscalefloor = xscalefloor
        self.yscalefloor = yscalefloor
        self.xscaleceiling = xscaleceiling
        self.yscaleceiling = yscaleceiling
        self.rotationfloor = rotationfloor
        self.rotationceiling = rotationceiling
        self.ceilingplane_a = ceilingplane_a
        self.ceilingplane_b = ceilingplane_b
        self.ceilingplane_c = ceilingplane_c
        self.ceilingplane_d = ceilingplane_d
        self.floorplane_a = floorplane_a
        self.floorplane_b = floorplane_b
        self.floorplane_c = floorplane_c
        self.floorplane_d = floorplane_d
        self.lightfloor = lightfloor
        self.lightceiling = lightceiling
        self.lightfloorabsolute = lightfloorabsolute
        self.lightceilingabsolute = lightceilingabsolute
        self.alphafloor = alphafloor
        self.alphaceiling = alphaceiling
        self.renderstylefloor = renderstylefloor
        self.renderstyleceiling = renderstyleceiling
        self.gravity = gravity
        self.lightcolor = lightcolor
        self.fadecolor = fadecolor
        self.desaturation = desaturation
        self.silent = silent
        self.nofallingdamage = nofallingdamage
        self.noattack = noattack
        self.dropactors = dropactors
        self.norespawn = norespawn
        self.soundsequence = soundsequence
        self.hidden = hidden
        self.waterzone = waterzone
        self.moreids = moreids
        self.damageamount = damageamount
        self.damagetype = damagetype
        self.damageinterval = damageinterval
        self.leakiness = leakiness
        self.damageterraineffect = damageterraineffect
        self.damagehazard = damagehazard
        self.floorterrain = floorterrain
        self.ceilingterrain = ceilingterrain
        self.floor_reflect = floor_reflect
        self.ceiling_reflect = ceiling_reflect
        self.fogdensity = fogdensity
        self.floorglowcolor = floorglowcolor
        self.floorglowheight = floorglowheight
        self.ceilingglowcolor = ceilingglowcolor
        self.ceilingglowheight = ceilingglowheight
        self.color_floor = color_floor
        self.color_ceiling = color_ceiling
        self.color_walltop = color_walltop
        self.color_wallbottom = color_wallbottom
        self.color_sprites = color_sprites
        self.coloradd_floor = coloradd_floor
        self.coloradd_ceiling = coloradd_ceiling
        self.coloradd_sprites = coloradd_sprites
        self.coloradd_walls = coloradd_walls
        self.colorization_floor = colorization_floor
        self.colorization_ceiling = colorization_ceiling
        self.noskywalls = noskywalls
        self.portal_ceil_blocksound = portal_ceil_blocksound
        self.portal_ceil_disabled = portal_ceil_disabled
        self.portal_ceil_nopass = portal_ceil_nopass
        self.portal_ceil_norender = portal_ceil_norender
        self.portal_ceil_overlaytype = portal_ceil_overlaytype
        self.portal_floor_blocksound = portal_floor_blocksound
        self.portal_floor_disabled = portal_floor_disabled
        self.portal_floor_nopass = portal_floor_nopass
        self.portal_floor_norender = portal_floor_norender
        self.portal_floor_overlaytype = portal_floor_overlaytype
        self.healthfloor = healthfloor
        self.healthfloorgroup = healthfloorgroup
        self.healthceiling = healthceiling
        self.healthceilinggroup = healthceilinggroup
        self.lm_sampledist_floor = lm_sampledist_floor
        self.lm_sampledist_ceiling = lm_sampledist_ceiling
        self.lm_dynamic = lm_dynamic
        super().__init__(kwargs={
            'heightfloor': self.heightfloor, 'heightceiling': self.heightceiling, 'texturefloor': self.texturefloor, 'textureceiling': self.textureceiling, 'lightlevel': self.lightlevel, 'special': self.special, 'id': self.id, 'comment': self.comment, 'xpanningfloor': self.xpanningfloor, 'ypanningfloor': self.ypanningfloor, 'xpanningceiling': self.xpanningceiling, 'ypanningceiling': self.ypanningceiling, 'xscalefloor': self.xscalefloor, 'yscalefloor': self.yscalefloor, 'xscaleceiling': self.xscaleceiling, 'yscaleceiling': self.yscaleceiling, 'rotationfloor': self.rotationfloor, 'rotationceiling': self.rotationceiling, 'ceilingplane_a': self.ceilingplane_a, 'ceilingplane_b': self.ceilingplane_b, 'ceilingplane_c': self.ceilingplane_c, 'ceilingplane_d': self.ceilingplane_d, 'floorplane_a': self.floorplane_a, 'floorplane_b': self.floorplane_b, 'floorplane_c': self.floorplane_c, 'floorplane_d': self.floorplane_d, 'lightfloor': self.lightfloor, 'lightceiling': self.lightceiling, 'lightfloorabsolute': self.lightfloorabsolute, 'lightceilingabsolute': self.lightceilingabsolute, 'alphafloor': self.alphafloor, 'alphaceiling': self.alphaceiling, 'renderstylefloor': self.renderstylefloor, 'renderstyleceiling': self.renderstyleceiling, 'gravity': self.gravity, 'lightcolor': self.lightcolor, 'fadecolor': self.fadecolor, 'desaturation': self.desaturation, 'silent': self.silent, 'nofallingdamage': self.nofallingdamage, 'noattack': self.noattack, 'dropactors': self.dropactors, 'norespawn': self.norespawn, 'soundsequence': self.soundsequence, 'hidden': self.hidden, 'waterzone': self.waterzone, 'moreids': self.moreids, 'damageamount': self.damageamount, 'damagetype': self.damagetype, 'damageinterval': self.damageinterval, 'leakiness': self.leakiness, 'damageterraineffect': self.damageterraineffect, 'damagehazard': self.damagehazard, 'floorterrain': self.floorterrain, 'ceilingterrain': self.ceilingterrain, 'floor_reflect': self.floor_reflect, 'ceiling_reflect': self.ceiling_reflect, 'fogdensity': self.fogdensity, 'floorglowcolor': self.floorglowcolor, 'floorglowheight': self.floorglowheight, 'ceilingglowcolor': self.ceilingglowcolor, 'ceilingglowheight': self.ceilingglowheight, 'color_floor': self.color_floor, 'color_ceiling': self.color_ceiling, 'color_walltop': self.color_walltop, 'color_wallbottom': self.color_wallbottom, 'color_sprites': self.color_sprites, 'coloradd_floor': self.coloradd_floor, 'coloradd_ceiling': self.coloradd_ceiling, 'coloradd_sprites': self.coloradd_sprites, 'coloradd_walls': self.coloradd_walls, 'colorization_floor': self.colorization_floor, 'colorization_ceiling': self.colorization_ceiling, 'noskywalls': self.noskywalls, 'portal_ceil_blocksound': self.portal_ceil_blocksound, 'portal_ceil_disabled': self.portal_ceil_disabled, 'portal_ceil_nopass': self.portal_ceil_nopass, 'portal_ceil_norender': self.portal_ceil_norender, 'portal_ceil_overlaytype': self.portal_ceil_overlaytype, 'portal_floor_blocksound': self.portal_floor_blocksound, 'portal_floor_disabled': self.portal_floor_disabled, 'portal_floor_nopass': self.portal_floor_nopass, 'portal_floor_norender': self.portal_floor_norender, 'portal_floor_overlaytype': self.portal_floor_overlaytype, 'healthfloor': self.healthfloor, 'healthfloorgroup': self.healthfloorgroup, 'healthceiling': self.healthceiling, 'healthceilinggroup': self.healthceilinggroup, 'lm_sampledist_floor': self.lm_sampledist_floor, 'lm_sampledist_ceiling': self.lm_sampledist_ceiling, 'lm_dynamic': self.lm_dynamic
        })
        