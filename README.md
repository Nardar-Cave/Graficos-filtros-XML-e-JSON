# Visualizador de Dados JSON e XML

Este é um aplicativo web desenvolvido em Flask que permite a visualização e análise de dados provenientes de arquivos JSON e XML em um único gráfico interativo. O aplicativo oferece recursos de filtragem por valores e datas, permitindo uma análise comparativa eficiente dos dados de ambas as fontes.

## 🎯 Objetivo

O principal objetivo deste projeto é fornecer uma interface única e intuitiva para visualizar e comparar dados provenientes de diferentes fontes (JSON e XML) em um único gráfico interativo, facilitando a análise e comparação dos dados.

## ✨ Características

- Interface web interativa
- Suporte a múltiplas fontes de dados (JSON e XML)
- Filtros dinâmicos por:
  - Valor mínimo
  - Valor máximo
  - Data inicial
  - Data final
- Gráfico interativo usando Plotly.js
- Diferenciação visual entre fontes de dados
- Atualização dinâmica do gráfico

## 🚀 Como Instalar e Executar

1. Clone o repositório:
```bash
git clone https://github.com/Nardar-Cave/Graficos-filtros-XML-e-JSON.git
cd nome-do-repo
```

2. Instale as dependências:
```bash
pip install flask
```

3. Execute o aplicativo:
```bash
python app.py
```

4. Acesse a aplicação em: http://localhost:5000

## 📁 Estrutura do Projeto

```
projeto/
│
├── app.py                 # Aplicação Flask principal
├── templates/
│   └── index.html        # Interface do usuário
├── data/
│   ├── dados.json        # Arquivo de dados JSON
│   └── dados.xml         # Arquivo de dados XML
└── README.md             # Este arquivo
```

## 📋 Formato dos Dados

### JSON
O arquivo JSON deve seguir estritamente o seguinte formato:
```json
[
    {
        "date": "2024-01-01",
        "value": 100
    },
    {
        "date": "2024-01-02",
        "value": 150
    }
]
```

### XML
O arquivo XML deve seguir estritamente o seguinte formato:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<data>
    <item>
        <date>2024-01-01</date>
        <value>90</value>
    </item>
    <item>
        <date>2024-01-02</date>
        <value>140</value>
    </item>
</data>
```

## ⚠️ Pontos de Atenção

1. **Formato das Datas**: 
   - As datas devem estar no formato "YYYY-MM-DD"
   - Datas em formato diferente causarão erro no processamento

2. **Localização dos Arquivos**:
   - Os arquivos de dados devem estar na pasta `data/`
   - Os nomes dos arquivos devem ser exatamente `dados.json` e `dados.xml`

3. **Valores Numéricos**:
   - Os valores devem ser numéricos
   - Não use strings para valores
   - Use ponto (.) como separador decimal, não vírgula

4. **Filtros de Data**:
   - Os filtros de data precisam ser inseridos manualmente
   - Por padrão, o sistema mostra todos os dados se nenhuma data for selecionada
   - As datas selecionadas devem estar dentro do intervalo dos dados disponíveis

## 🚨 Limitações

1. **Processamento de Dados**:
   - Não suporta arquivos muito grandes (recomendado até 10MB)
   - Processamento síncrono (pode ser lento para grandes volumes de dados)

2. **Formato dos Dados**:
   - Não suporta formatos diferentes dos especificados acima
   - Não realiza validação profunda dos dados
   - Não suporta dados aninhados ou complexos

3. **Interface**:
   - Necessidade de inserção manual das datas para filtragem
   - Não possui persistência dos filtros (reset ao recarregar a página)
   - Não suporta múltiplos gráficos simultaneamente

4. **Arquivos**:
   - Não suporta upload dinâmico de arquivos
   - Nomes e localização dos arquivos são fixos
   - Não suporta outros formatos além de JSON e XML

## 🛠️ Melhorias Futuras

- Implementar upload dinâmico de arquivos
- Adicionar suporte a outros formatos de dados
- Implementar validação mais robusta dos dados
- Adicionar persistência dos filtros
- Implementar processamento assíncrono para grandes volumes de dados
- Adicionar mais tipos de visualizações
- Implementar exportação dos dados filtrados

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork do projeto e enviar suas pull requests.

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request
