
class EndPoint:
    BASE_URI_API = "https://bookstore.toolsqa.com/BookStore/v1/Books"
    BASE_URI_UI = "https://www.flipkart.com/"

    isbn = "9781449325862"
    title = "Git Pocket Guide"
    subTitle = "A Working Introduction"
    author = "Richard E. Silverman"
    publish_date = "2020-06-04T08:48:39.000Z"
    publisher = "O'Reilly Media"
    pages = 234
    description = "This pocket guide is the perfect on-the-job companion to Git, the distributed version control system. It provides a compact, readable introduction to Git for new users, as well as a reference to common commands and procedures for those of you with Git exp"
    website = "http://chimera.labs.oreilly.com/books/1230000000561/index.html"

    ProductSearch = "samsung galaxy m31 6gb 64gb"


class Flipkart:
    LoginPopupCancel = "//button[contains(text(),'✕')]"
    SearchTextBox = "//div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]"
    SearchButton = "//div[2]/div[2]/form[1]/div[1]/button[1]/*[1]"
    ProductLink = "//div[contains(text(),'SAMSUNG Galaxy M31 (Ocean Blue, 64 GB)')]"
    ProductPrice = "//div[3]/div[1]/div[4]/div[1]/div[1]/div[1]"
    AddToCartButton = "//div[1]/div[2]/div[1]/ul[1]/li[1]/button[1]"
    CartAddQuantity = "//button[@class='_23FHuj'][2]"
    CartTotalPrice = "//div[1]/span[1]/div[1]/div[1]/span[1]"


class Amazon:
    SearchTextBox = "//input[@id='twotabsearchtextbox']"
    SearchButton = "//input[@id='nav-search-submit-button']"
    ProductLink = "//span[contains(text(),'Samsung Galaxy M31 6GB 64GB (Ocean Blue)')]"
    ProductPrice = "//span[@id='priceblock_ourprice']"
    AddToCartButton = "//input[@id='add-to-cart-button']"
    CartTotalPrice = "//div[1]/div[1]/div[1]/div[1]/span[1]/span[2]"

