# DevLukeOps

Este projeto demonstra habilidades em DevOps com uma infraestrutura no Azure, utilizando Terraform, Ansible, Docker, GitHub Actions, Prometheus, Grafana e scripts em Python e Bash.

## Fases do Projeto

### Fase 1: Infraestrutura na Azure
- Configuração de uma VM no Azure usando Terraform.
- Provisionamento com Ansible.
- Status: Concluído.

### Fase 2: Monitoramento com Prometheus e Grafana
- Configuração de Prometheus e Grafana em contêineres Docker.
- Status: Concluído.

### Fase 3: Aplicação de Teste Simples
- Desenvolvimento de uma API Python com Flask e SQLite na porta 5110.
- Integração com Prometheus para exposição de métricas (`request_count_total`).
- Criação de um dashboard no Grafana para visualizar a taxa de requisições (`rate(request_count_total[5m])`).
- Ambiente migrado para VM Rocky Linux 9.5 devido a problemas com contêineres aninhados.
- Status: Concluído.

### Fase 4: Automação com CI/CD
- Implementação de pipelines com GitHub Actions.
- Status: Em andamento.

## Configuração Atual
- **Ambiente**: VM Rocky Linux 9.5 (IP: 10.0.2.15).
- **Serviços**:
  - Prometheus: Porta 9090 (mapeada como 9090 na VM).
  - Grafana: Porta 3000 (mapeada como 3000 na VM).
  - API: Porta 5110 (mapeada como 5110 na VM).
- **Acesso**: (adapte ao ip da sua maquina/VM ou use localhost)
  - API: `http://10.0.2.15:5110/api` (exibe contagem de visitas).
  - Métricas: `http://10.0.2.15:5110/metrics`.
  - Prometheus: `http://10.0.2.15:9090`.
  - Grafana: `http://10.0.2.15:3000` (dashboard "DevLukeOps Dashboard" criado).

## Instruções
1. Clone o repositório: `git clone git@github.com:lucasgesso/DevLukeOps.git`.
2. Navegue para o diretório: `cd DevLukeOps`.
5. Adicione o usuário ao grupo docker: `sudo usermod -aG docker $USER` e faça logout/login.
4. Inicie os serviços: `docker compose up -d`.
5. Acesse os serviços conforme os endereços acima(adaptando ao ip da sua maquina, ou maquina virtual. https://localhost:xxxx também funciona).


## Notas
- Ajuste no `prometheus.yml` de `host.docker.internal:5110` para `app:5110` resolveu problemas de rede na VM.
- O dashboard no Grafana exibe a taxa de requisições da API em tempo real.

## TODO
- **Fase 5**: Configuração com Ansible
- **Fase 6**: Pipeline CI/CD com GitHub Actions
- **Fase 7**: Fase 7: Monitoramento Completo
- **Fase 8**: Fase 8: Finalização e Polimento

## Lucas Gesso