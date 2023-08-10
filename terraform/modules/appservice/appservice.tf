resource "azurerm_service_plan" "test" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  os_type             = "Windows"
  sku_name            = "B1"
}

resource "azurerm_windows_web_app" "test" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  service_plan_id     = azurerm_service_plan.test.id

  site_config {
    remote_debugging_enabled = true
    always_on = false
    application_stack {
      dotnet_version = "v6.0"
    }
  }

  app_settings = {
    WEBSITE_RUN_FROM_PACKAGE = 1,
    SCM_DO_BUILD_DURING_DEPLOYMENT = true

}
}