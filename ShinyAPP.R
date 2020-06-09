library(shiny)
library(shinydashboard)
library(ggplot2)
library(scales)
library(shinythemes)


cases = read.csv("covid19_confirmed_cases.csv")
deaths = read.csv("covid19_deaths.csv")
recovered = read.csv("covid19_recovered.csv")




options = subset(cases, select=-c(X, Week))

ui <- fluidPage(
  tags$style(HTML("
    .tabbable > .nav > li > a                  {background-color: lightblue;  color:grey}
    .tabbable > .nav > li[class=active]    > a {background-color: lightblue; color:black}
  ")),
  
  titlePanel("Covid_19 Dashboard"),
  
  sidebarLayout(sidebarPanel(selectInput("country", "Select the Country",
                           c(colnames(options)))),
  mainPanel(tabsetPanel(
    type = 'tab',
    tabPanel("Up to Date Data", tableOutput("Covid19")),
    tabPanel("Number of Confirmed Cases", plotOutput("cases_plot")),
    tabPanel("Number of Deaths", plotOutput("deaths_plot")),
    tabPanel("Number of Recovered Patients", plotOutput("recovered_plot")),
    tabPanel("Recovery Ratio", plotOutput("recovery_ratio")),
    tabPanel("Mortality Rate", plotOutput("mortality_rate"))
  ))))



server <- function(input, output){
  
  output$Covid19 <- renderTable(
    cases[, c("Week", input$country)]
  )
  
  output$cases_plot <- renderPlot({
    ggplot(data=cases, aes(x=deaths$Week, y= cases[[input$country]])) +
      geom_line()+
      geom_point(shape=17, size=3)+
      labs(title = "Confirmed cases of Covid-19", x = "Number of Weeks", y = "Number of Cases")
  })
  
  output$deaths_plot <- renderPlot({
    ggplot(data=deaths, aes(x=deaths$Week, y= deaths[[input$country]])) +
      geom_line()+
      geom_point(shape=17, size=3)+
      labs(title = "Deaths due to Covid-19", x = "Number of Weeks", y = "Number of Deaths")
  })
  
  
  output$recovered_plot <- renderPlot({
    ggplot(data=recovered, aes(x=deaths$Week, y= recovered[[input$country]])) +
      geom_line()+
      geom_point(shape=17, size=3)+
      labs(title = "Number of Patients Recovered from Covid-19", x = "Number of Weeks", y = "Number of Patients Recovered")
  })
  
  output$recovery_ratio <- renderPlot({
    ggplot(data=recovered, aes(x=deaths$Week, y= recovered[[input$country]] / cases[[input$country]])) +
      geom_line()+
      geom_point(shape=17, size=3)+
      labs(title = "Recovery Rate of Covid-19", x = "Number of Weeks", y = "Recovery Ratio")
  })
  
  output$mortality_rate <- renderPlot({
    ggplot(data=recovered, aes(x=deaths$Week, y= deaths[[input$country]] / cases[[input$country]])) +
      geom_line()+
      geom_point(shape=17, size=3)+
      labs(title = "Mortality Rate of Covid-19", x = "Number of Weeks", y = "Mortality Rate")
  })
  
  
}

shinyApp(ui, server)
 

  