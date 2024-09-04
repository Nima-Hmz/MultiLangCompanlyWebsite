from .models import ContactUs
from .template_manager import language_switcher

def current_language(request):
    """
    Context processor to inject the current language into templates.
    """
    # Get the current language from the GET parameters, cookies, or default to 'en'
    # plus contactus 

    lang = request.GET.get('lang', 'fa') 
    contactus = ContactUs.objects.first()
    output = {'current_lang': lang}
    output.update(language_switcher(contactus, lang, "contact"))
    output['contact_phone'] = contactus.phone_number
    output['contact_email'] = contactus.email 
    output['contact_location'] = contactus.location

    return output