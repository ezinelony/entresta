
def getReferrer(request,exclude):
    ref="/"
    if 'HTTP_REFERER' in request.META and 'ref' in request.session:
        if exclude not in request.META['HTTP_REFERER']:
            ref=request.META['HTTP_REFERER']
    else:        
        if not 'ref' in request.session:
            if 'HTTP_REFERER' in request.META:
                ref=request.META['HTTP_REFERER']
            else :
                ref="/"     
        elif 'ref' in request.session:
            ref=request.session['ref'] 
        else :
            ref="/"     
    return ref    