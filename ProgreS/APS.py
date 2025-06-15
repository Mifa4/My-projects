#v 0.01 do only one think

#hosts = r'C:\Windows\System32\drivers\etc\hosts' 
redirect_url = '192.168.1.240'
#.write(f'{redirect_url} {site}\n')
'''
with open(hosts,'r+') as sites:
        src = sites.readlines()
        sites.seek(0)

        for line in src:
            if not any(site in line for site in blocking):
                sites.write(line)
        sites.truncate()
'''
hosts = r'C:\Users\Елена\Documents\GitHub\My-projects\ProgreS\hosts.txt' 

print('Давай быть более продуктивными!')
print('\\s - основные настройки этого приложения.')
print('\\b [group] - заблокировать сайт.')
print('\\ub [group] - разблокировать сайт (необходим пароль).')
print('\\g [name] - добавить групу сайтов (необходим пароль).')
print('\\gs [name] - настройки групы сайтов (необходим пароль).')
def BlockSite(hosts,url,site):
        was = ''
        again = False
        with open(hosts,'r+')as file:
                was = file.readlines()
                for i in was:
                        if i == f'{url} {site}':
                                again = True
        with open(hosts,'w+')as file:
                if again == False:
                        if len(was) >= 1:
                                was.append(f'\n{url} {site}')
                        else:
                                was.append(f'{url} {site}')
                file.writelines(was)
BlockSite(hosts,redirect_url,'youtube.com')