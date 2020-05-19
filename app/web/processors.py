from app.web.models import BanerPrincipal, CatDepo
def social_banner(request):
    text_emil=""
    text_envio=""
    text_telefono=""
    email=BanerPrincipal.objects.filter(bp_tipo='1').first()
    info_envio=BanerPrincipal.objects.filter(bp_tipo='2').first()
    telefono=BanerPrincipal.objects.filter(bp_tipo='3').first()

    social=BanerPrincipal.objects.exclude(bp_tipo__in=['1', '2', '3'])
    if email != None:
        text_emil=email.bp_url
    if info_envio != None:
        text_envio=info_envio.bp_url
    if telefono != None:
        text_telefono=telefono.bp_url

    return {'email':text_emil,'info_envio':text_envio,'text_tel':text_telefono, 'social':social}


def depo_cat(request):
    query=CatDepo.objects.filter(cd_visible=True)
    return {'query_cd':query}
