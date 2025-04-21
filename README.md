# DSDC Tecnologia da Informação

Site institucional bilíngue (Português/Inglês) da DSDC Tecnologia da Informação (Dos Santos e De Carvalho Tecnologia da Informação Ltda.).

## Funcionalidades
- Apresentação institucional
- Ênfase em bots de atendimento via WhatsApp e automação de processos de negócio
- Formulário de coleta de leads
- Layout responsivo, moderno, com paleta de cores pastel
- Suporte a Português e Inglês

## Como rodar localmente

### Pré-requisitos
- Python 3.10+
- [UV](https://github.com/astral-sh/uv) (gerenciador de pacotes)

```bash
uv venv .venv
.venv/Scripts/activate  # Windows
uv pip install -r requirements.txt
cd app
flask run
```

Acesse http://localhost:5000

### Compilando traduções
Para atualizar traduções após editar arquivos `.po`:

```bash
pybabel compile -d translations
```

## Como rodar via Docker

### Build e execução
```bash
docker build -t dsdc-site .
docker run -d -p 5000:5000 --name dsdc-site dsdc-site
```

Acesse http://IP_DA_VPS:5000

## Deploy em stack Portainer (docker-compose)

Exemplo de `docker-compose.yml`:

```yaml
version: '3.8'
services:
  dsdc-site:
    build: .
    container_name: dsdc-site
    restart: unless-stopped
    ports:
      - "5000:5000"
    environment:
      - FLASK_RUN_HOST=0.0.0.0
      - FLASK_APP=app
```

## Configuração de domínio e HTTPS

Para domínio próprio e HTTPS, recomenda-se utilizar o [nginx-proxy](https://github.com/nginx-proxy/nginx-proxy) + [acme-companion](https://github.com/nginx-proxy/acme-companion) para certificados SSL automáticos Let's Encrypt.

Exemplo de stack:

```yaml
version: '3.8'
services:
  nginx-proxy:
    image: jwilder/nginx-proxy
    container_name: nginx-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/tmp/docker.sock:ro
      - ./certs:/etc/nginx/certs:ro
      - ./vhost.d:/etc/nginx/vhost.d
      - ./html:/usr/share/nginx/html
    restart: unless-stopped

  acme-companion:
    image: nginxproxy/acme-companion
    container_name: acme-companion
    depends_on:
      - nginx-proxy
    environment:
      - DEFAULT_EMAIL=seu@email.com
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./certs:/etc/nginx/certs:rw
      - ./vhost.d:/etc/nginx/vhost.d
      - ./html:/usr/share/nginx/html
      - ./acme:/etc/acme.sh
    restart: unless-stopped

  dsdc-site:
    build: .
    container_name: dsdc-site
    environment:
      - VIRTUAL_HOST=seudominio.com.br
      - LETSENCRYPT_HOST=seudominio.com.br
      - LETSENCRYPT_EMAIL=seu@email.com
      - FLASK_RUN_HOST=0.0.0.0
      - FLASK_APP=app
    expose:
      - "5000"
    restart: unless-stopped
```

Altere `seudominio.com.br` e `seu@email.com` para seus dados.

## Customização
- Para trocar a imagem de background: substitua `app/static/img/tech-bg.jpg` por outra de sua preferência.
- Para adicionar um logo: coloque seu arquivo em `app/static/img/` e edite o template `index.html`.
- Para alterar textos/traduções: edite os arquivos `.po` em `app/translations/` e recompile.

## Contato
Para dúvidas ou suporte, entre em contato com a equipe DSDC.
