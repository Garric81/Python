s = Server(ad_domain, use_ssl=True, port=636)  # Адрес домена, шифрование, порт
c = Connection(s, ad_admin, ad_password)

# Создание учётной записи в домене (Active Directory)
def create_ad(first, last, uis_login, phone, position, domain_uis, uis_password):
    c.bind()

    if not c.add('cn=' + first + ' ' + last + ', ou=jsoc-admin, dc=rt-solar, dc=local', 'user',
                 {'displayName': first + ' ' + last,  # Отображаемое имя
                  'givenName': first,  # Имя
                  'sn': last,  # Фамилия
                  'userPrincipalName': uis_login + '@domain.local',  # Имя входа пользователя
                  'sAMAccountName': uis_login,  # Имя входа пользователя (пред-Windows 2000)
                  'mobile': phone,  # Телефон
                  'title': position,  # Должность
                  'mail': uis_login + '@' + domain_uis,  # E-mail
                  'info': uis_password  # Заметки
                  }):
        return 'Не удалось создать учётную запись в AD'

    # Разблокируем учётную запись
    c.extend.microsoft.unlock_account(
        user='cn=' + first + ' ' + last + ', ou=jsoc-admin, dc=rt-solar, dc=local')

    # Устанавливаем пароль
    if not c.extend.microsoft.modify_password(user='cn=' + first + ' ' + last + ', ou=jsoc-admin, dc=rt-solar, dc=local',
                                              new_password=uis_password, old_password=None):
        return 'Не удалось установить пароль'

    # Определяем атрибуты
    change_uac_attribute = {
        "userAccountControl": (MODIFY_REPLACE, [512])}
    # 512: Normal account
    # 514: Disable account
    # 65536: Normal account + don't expire password

    # Устанавливаем атрибуты
    if not c.modify('cn=' + first + ' ' + last + ', ou=Подразделение, dc=domain, dc=local', changes=change_uac_attribute):
        return 'Не удалось установить атрибуты'

    # Добавляем в группы
    ad_add_members_to_groups(c, 'cn=' + first + ' ' + last + ', ou=jsoc-admin, dc=rt-solar, dc=local',
                             'cn=Группа, ou=jsoc-admin, dc=rt-solar, dc=local')
    c.unbind()
    return 'Done'