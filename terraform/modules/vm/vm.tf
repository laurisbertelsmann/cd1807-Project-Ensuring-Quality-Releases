resource "azurerm_network_interface" "vm_nic" {
  name                = "${var.vm_name}-nic"
  location            = var.location
  resource_group_name = var.resource_group

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip
  }
}

data "azurerm_image" "custom-image" {
  name                = "udacity-vm-v2" 
  resource_group_name = "rg-udacity-storage-final-project"
}



resource "azurerm_linux_virtual_machine" "linux-vm" {
  name                = "${var.vm_name}"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS2_v2"
  network_interface_ids = [azurerm_network_interface.vm_nic.id]
  source_image_id = data.azurerm_image.custom-image.id
  disable_password_authentication = false
  admin_username      = "lauris"
  admin_password = "Udacity@123"


  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
}