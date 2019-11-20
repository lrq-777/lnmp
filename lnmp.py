from  fabric.api import *
env.user = 'root'
env.hosts = ['192.168.227.110']



@task()
def envirement():
    run('systemctl stop firewalld')
@task()
def repo():
    run('yum -y install gcc zlib* openssl-devel gcc-c++ pcre-devel')
    run('rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm')
    run('rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm')
    run('yum -y install wget')
@task()
def nginx():
    with cd('/root'):
        run('wget http://nginx.org/download/nginx-1.13.7.tar.gz')
        run('tar -xvf nginx-1.13.7.tar.gz')
        with cd('/root/nginx-1.13.7'):
            run('./configure --with-http_stub_status_module --with-http_ssl_module  --prefix=/usr/local/nginx')
            run('make && make install')
@task()
def php():
    run('yum -y install php71w php71w-cli php71w-common php71w-devel php71w-embedded php71w-gd php71w-mbstring php71w-pdo php71w-xml php71w-fpm php71w-mysqlnd php71w-opcache php71w-mcrypt php71w-pecl-memcached php71w-pecl-mongodb php71w-pecl-redis')
@task()
def mariadb():
    run('yum -y install mariadb-server mariadb')

@task()
def restart():
    run('/usr/local/nginx/sbin/nginx  -c /usr/local/nginx/conf/nginx.conf')
    run('systemctl start php-fpm')
    run('systemctl start mariadb')

def huanjing():
    execute(envirement)
    execute(repo)
def install():
    execute(nginx)
    execute(php)
    execute(mariadb)
def sys_start():
    execute(restart)
while True:
    app = input("数字")
    if app == '1':
        huanjing()
    elif app == '2':
        install()
    elif app == '3':
        sys_start()
    else:
        break
