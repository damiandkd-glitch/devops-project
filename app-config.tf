resource "kubernetes_config_map" "app_settings" {
  metadata {
    name      = "app-settings-terraform"
    namespace = "default"
  }
  data = {
    ENVIRONMENT = "production"
    LOG_LEVEL   = "info"
    MANAGED_BY  = "terraform"
  }
}