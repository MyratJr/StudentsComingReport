from .models import Ishgarler as ter
from .models import Wezipeler as ret

for i in range(1,10):
    saving=ter(
        at= input('at>>'),
        wezipe=ret.objects.get(Wezipe_at=input('wezipe>>')),
        gelen_wagty={None:None},
        giden_wagty={None:None},
        is_bashlayar=input('wagt1>>'),
        is_gutaryar=input('wagt2>>'),
        obed_bashlayar=input('wagt3>>'),
        obed_gutaryar=input('wagt4>>'),
        barkod_san=int(input('barkod>>'))
        )
    saving.save()