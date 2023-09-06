from .mixins import PropertyMixin


class Sidedef(PropertyMixin):
    def __init__(self, offsetx=None, offsety=None, texturetop=None, texturebottom=None, texturemiddle=None, sector=None, comment=None, scalex_top=None, scaley_top=None, scalex_mid=None, scaley_mid=None, scalex_bottom=None, scaley_bottom=None, offsetx_top=None, offsety_top=None, offsetx_mid=None, offsety_mid=None, offsetx_bottom=None, offsety_bottom=None, light=None, lightabsolute=None, light_top=None, lightabsolute_top=None, light_mid=None, lightabsolute_mid=None, light_bottom=None, lightabsolute_bottom=None, lightfog=None, nofakecontrast=None, smoothlighting=None, clipmidtex=None, wrapmidtex=None, nodecals=None, nogradient_top=None, flipgradient_top=None, clampgradient_top=None, useowncolors_top=None, uppercolor_top=None, lowercolor_top=None, nogradient_mid=None, flipgradient_mid=None, clampgradient_mid=None, useowncolors_mid=None, uppercolor_mid=None, lowercolor_mid=None, nogradient_bottom=None, flipgradient_bottom=None, clampgradient_bottom=None, useowncolors_bottom=None, uppercolor_bottom=None, lowercolor_bottom=None, useowncoloradd_top=None, useowncoloradd_mid=None, useowncoloradd_bottom=None, coloradd_top=None, coloradd_mid=None, coloradd_bottom=None, colorization_top=None, colorization_mid=None, colorization_bottom=None):
        self.offsetx = offsetx
        self.offsety = offsety
        self.texturetop = texturetop
        self.texturebottom = texturebottom
        self.texturemiddle = texturemiddle
        self.sector = sector
        self.comment = comment
        self.scalex_top = scalex_top
        self.scaley_top = scaley_top
        self.scalex_mid = scalex_mid
        self.scaley_mid = scaley_mid
        self.scalex_bottom = scalex_bottom
        self.scaley_bottom = scaley_bottom
        self.offsetx_top = offsetx_top
        self.offsety_top = offsety_top
        self.offsetx_mid = offsetx_mid
        self.offsety_mid = offsety_mid
        self.offsetx_bottom = offsetx_bottom
        self.offsety_bottom = offsety_bottom
        self.light = light
        self.lightabsolute = lightabsolute
        self.light_top = light_top
        self.lightabsolute_top = lightabsolute_top
        self.light_mid = light_mid
        self.lightabsolute_mid = lightabsolute_mid
        self.light_bottom = light_bottom
        self.lightabsolute_bottom = lightabsolute_bottom
        self.lightfog = lightfog
        self.nofakecontrast = nofakecontrast
        self.smoothlighting = smoothlighting
        self.clipmidtex = clipmidtex
        self.wrapmidtex = wrapmidtex
        self.nodecals = nodecals
        self.nogradient_top = nogradient_top
        self.flipgradient_top = flipgradient_top
        self.clampgradient_top = clampgradient_top
        self.useowncolors_top = useowncolors_top
        self.uppercolor_top = uppercolor_top
        self.lowercolor_top = lowercolor_top
        self.nogradient_mid = nogradient_mid
        self.flipgradient_mid = flipgradient_mid
        self.clampgradient_mid = clampgradient_mid
        self.useowncolors_mid = useowncolors_mid
        self.uppercolor_mid = uppercolor_mid
        self.lowercolor_mid = lowercolor_mid
        self.nogradient_bottom = nogradient_bottom
        self.flipgradient_bottom = flipgradient_bottom
        self.clampgradient_bottom = clampgradient_bottom
        self.useowncolors_bottom = useowncolors_bottom
        self.uppercolor_bottom = uppercolor_bottom
        self.lowercolor_bottom = lowercolor_bottom
        self.useowncoloradd_top = useowncoloradd_top
        self.useowncoloradd_mid = useowncoloradd_mid
        self.useowncoloradd_bottom = useowncoloradd_bottom
        self.coloradd_top = coloradd_top
        self.coloradd_mid = coloradd_mid
        self.coloradd_bottom = coloradd_bottom
        self.colorization_top = colorization_top
        self.colorization_mid = colorization_mid
        self.colorization_bottom = colorization_bottom
        super().__init__(kwargs={
            'offsetx': self.offsetx, 'offsety': self.offsety, 'texturetop': self.texturetop, 'texturebottom': self.texturebottom, 'texturemiddle': self.texturemiddle, 'sector': self.sector, 'comment': self.comment, 'scalex_top': self.scalex_top, 'scaley_top': self.scaley_top, 'scalex_mid': self.scalex_mid, 'scaley_mid': self.scaley_mid, 'scalex_bottom': self.scalex_bottom, 'scaley_bottom': self.scaley_bottom, 'offsetx_top': self.offsetx_top, 'offsety_top': self.offsety_top, 'offsetx_mid': self.offsetx_mid, 'offsety_mid': self.offsety_mid, 'offsetx_bottom': self.offsetx_bottom, 'offsety_bottom': self.offsety_bottom, 'light': self.light, 'lightabsolute': self.lightabsolute, 'light_top': self.light_top, 'lightabsolute_top': self.lightabsolute_top, 'light_mid': self.light_mid, 'lightabsolute_mid': self.lightabsolute_mid, 'light_bottom': self.light_bottom, 'lightabsolute_bottom': self.lightabsolute_bottom, 'lightfog': self.lightfog, 'nofakecontrast': self.nofakecontrast, 'smoothlighting': self.smoothlighting, 'clipmidtex': self.clipmidtex, 'wrapmidtex': self.wrapmidtex, 'nodecals': self.nodecals, 'nogradient_top': self.nogradient_top, 'flipgradient_top': self.flipgradient_top, 'clampgradient_top': self.clampgradient_top, 'useowncolors_top': self.useowncolors_top, 'uppercolor_top': self.uppercolor_top, 'lowercolor_top': self.lowercolor_top, 'nogradient_mid': self.nogradient_mid, 'flipgradient_mid': self.flipgradient_mid, 'clampgradient_mid': self.clampgradient_mid, 'useowncolors_mid': self.useowncolors_mid, 'uppercolor_mid': self.uppercolor_mid, 'lowercolor_mid': self.lowercolor_mid, 'nogradient_bottom': self.nogradient_bottom, 'flipgradient_bottom': self.flipgradient_bottom, 'clampgradient_bottom': self.clampgradient_bottom, 'useowncolors_bottom': self.useowncolors_bottom, 'uppercolor_bottom': self.uppercolor_bottom, 'lowercolor_bottom': self.lowercolor_bottom, 'useowncoloradd_top': self.useowncoloradd_top, 'useowncoloradd_mid': self.useowncoloradd_mid, 'useowncoloradd_bottom': self.useowncoloradd_bottom, 'coloradd_top': self.coloradd_top, 'coloradd_mid': self.coloradd_mid, 'coloradd_bottom': self.coloradd_bottom, 'colorization_top': self.colorization_top, 'colorization_mid': self.colorization_mid, 'colorization_bottom': self.colorization_bottom
        })
        