if (!require(pacman)) install.packages("pacman")
pacman::p_load(tidyverse, readxl, shiny)

# Função para carregar os dados do Excel
carregar_dados <- function() {
  read_xlsx("escolas.xlsx")
}

# Função para salvar os dados no Excel (opcional)
salvar_dados <- function(dados) {
  write_xlsx(dados, "escolas.xlsx")
}

# Interface do usuário
ui <- fluidPage(
  titlePanel("CRM para Escolas"),
  sidebarLayout(
    sidebarPanel(
      textInput("codigo", "Código da Escola"),
      actionButton("buscar", "Buscar Escola"),
      uiOutput("infoEscola"),
      selectInput("status", "Status", 
                  choices = c("Aguardando Contato", "Chamada Agendada", "Chamada Não Atendida", "Coleta de Dados Concluída")),
      actionButton("atualizar", "Atualizar Status")
    ),
    mainPanel(
      h3("Kanban de Status"),
      uiOutput("kanban")
    )
  )
)

# Lógica do servidor
server <- function(input, output, session) {
  # Carregar dados do Excel
  dados <- reactiveVal(carregar_dados())
  
  # Buscar escola pelo código
  observeEvent(input$buscar, {
    escola <- dados() %>% filter(codigo_escola == input$codigo)
    output$infoEscola <- renderUI({
      if (nrow(escola) > 0) {
        tagList(
          h3(escola$nome_escola),
          p(paste("Diretor:", escola$nome_diretor)),
          p(paste("Telefone:", escola$telefone)),
          p(paste("Status atual:", escola$status))
        )
      } else {
        p("Escola não encontrada.")
      }
    })
  })
  
  # Atualizar status da escola
  observeEvent(input$atualizar, {
    novos_dados <- dados()
    novos_dados <- novos_dados %>%
      mutate(status = ifelse(codigo_escola == input$codigo, input$status, status))
    dados(novos_dados)
    salvar_dados(novos_dados)  # Salva as alterações no Excel (opcional)
    showNotification("Status atualizado com sucesso!")
  })
  
  # Exibir kanban
  output$kanban <- renderUI({
    status_counts <- dados() %>% count(status)
    fluidRow(
      lapply(unique(dados()$status), function(s) {
        column(3, 
               h4(s),
               p(paste("Escolas:", status_counts %>% filter(status == s) %>% pull(n)))
        )
      })
    )
  })
}

# Rodar a aplicação
shinyApp(ui, server)
