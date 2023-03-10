class BaseAdminModal(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.get_fields()
                if field.__class__.__name__ != 'ManyToOneRel' and not field.many_to_many and
                field.name not in ['creation_date', 'creator', 'edit_date', 'editor']
                ] + ['creation_date', 'creator', 'edit_date', 'editor']

    def get_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.get_fields()
                if field.__class__.__name__ != 'ManyToOneRel' and
                field.name not in ['id', 'creation_date', 'creator', 'edit_date', 'editor',
                                   'users', 'divisions', 'enterprises']
                ] + ['users', 'divisions', 'enterprises',
                     'creation_date', 'creator', 'edit_date', 'editor']
      
      
class BaseModel_AU(models.Model):
    creation_date = models.DateTimeField(verbose_name='Дата создания', null=True, blank=True, auto_now_add=True)
    creator = models.ForeignKey('app_user.SysUser', related_name="%(app_label)s_%(class)s_related_cr",
                              null=True, blank=True, on_delete=models.PROTECT,
                              verbose_name='Добавил')
    edit_date = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, null=True, blank=True)
    editor = models.ForeignKey('app_user.SysUser', related_name="%(app_label)s_%(class)s_related_ed",
                             null=True, blank=True, on_delete=models.PROTECT,
                             verbose_name='Изменил')

def save(self, *args, **kwargs):
  """ Переопределение функции save для автоматического
          создания редактора и создателя пользователя"""

  user = get_current_user()
  if self.creator is None:
      self.creator = user

  self.editor = user

  super().save(*args, **kwargs)

class Meta:
  abstract = True
      
