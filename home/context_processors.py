def current_language(request):
    """
    Context processor to inject the current language into templates.
    """
    # Get the current language from the GET parameters, cookies, or default to 'en'
    lang = request.GET.get('lang', 'fa') 
    return {'current_lang': lang}