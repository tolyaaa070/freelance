from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Skill)
class ProductTranslationOptions(TranslationOptions):
    fields = ('skill_name', )


@register(UserProfile)
class ProductTranslationOptions(TranslationOptions):
    fields = ('bio','role')


@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Project)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title','description','status')


@register(Offer)
class ProductTranslationOptions(TranslationOptions):
    fields = ('message',)



