from .models import FirstTitle, ContactUs, AboutUs, Services


def language_switcher(model_object, lang, usecase):
	# extension for choosing the right attribute from the model

	context = {

		f'{usecase}_title':model_object.get_title(lang),
		f'{usecase}_description':model_object.get_description(lang)

	}

	return context