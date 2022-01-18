<h1><img src="/images/deal.png" alt="deal imagem">Deals of the Day</h1>
<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->
<p>
<img src="/images/python.png" alt="python imagem"/>
<img src="/images/scrapy.png" alt="scrapy imagem"/>
<img src="https://img.shields.io/badge/python-scrapy-green" alt="Bitbucket open pull requests" />
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/david-adds/mercadolivre-scraper?style=plastic">
<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/david-adds/mercadolivre-scraper?style=plastic">
<img alt="GitHub forks" src="https://img.shields.io/github/forks/david-adds/mercadolivre-scraper?style=social">
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/david-adds/mercadolivre-scraper?style=social">
</p>


<p>This is a web scraper, using the Python framework Scrapy, built to extract data such as price and product name from the Deals of the Day section on Mercado Livre website.</p>

<img src="/images/deals-of-the-day.png" alt="ml imagem">

<h2><img src="/images/web-crawler.png" alt="wcrwl imagem"> What Data Do We Want to Scrape?</h2>
<ul>
<li><input type="checkbox" checked="" enabled="" /> Product Name</li>
<li><input type="checkbox" checked="" enabled="" /> Original Price</li>
<li><input type="checkbox" checked="" enabled="" /> Current Price</li>
<li><input type="checkbox" checked="" enabled="" /> Product Url</li>
<li><input type="checkbox" checked="" enabled="" /> Data Extraction Date</li>
</ul>

<h4> Note: The scraper handles pagination and extracts the aforementioned data throughout the entire Deals of the Day section.</h4>

<h2>💻 Requirements</h2>
<p>Before you start, please check if you have met these few basic requirements:</p>
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
<ul>
<li>Installed the latest stable python version (Python 3.7 or later).</li>
<li>Created a virtual enviroment to run the ScraPy framework on your machine.</li>
<li>Installed Scrapy 1.6 or a later stable version.</li>

<h4> Note: It is strongly recommended that you install Scrapy in a dedicated virtualenv, to avoid conflicting with your system packages.</h4>
</ul>
<h2> Getting Started</h2>
<p><strong>From terminal</strong></p>

<ol>
<li>Create an Enviroment:</li>
</ol>

<pre><code>
$ mkdir virtual-enviroments
$ cd virtual-enviroments
$ python3 -m venv venv
</code></pre>

<ol start="2">
<li>Activate it:<br />
Linux/macOS</li>
</ol>
<pre><code>$ source venv/bin/activate
</code></pre>
<ol start="3">
<li>Install the Scrapy framework:</li>
</ol>
<pre><code>$ pip install Scrapy
</code></pre>

<h2>🚀 How to Use:</h2>

<p>Clone this repository into your workspace:</p>

<pre><code>$ git clone https://github.com/david-adds/mercadolivre-scraper.git
</code></pre>
<p>Once you have cloned the repository, open it up so you can run the scraper.</p>
<pre><code>$ cd mercadolivre-scraper
</code></pre>
<p>Then, run the spider to scrape the data:</p>
<pre><code>$ scrapy crawl deals
</code></pre>

<div id="voltarTopo">
	<a href="#" id="up">UP</a>
</div>

$