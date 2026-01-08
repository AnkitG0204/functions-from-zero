import click
from mylib.bot import scrape

@click.command()
@click.option('--name', prompt = 'Wikipedia page to scrape',
              help = 'Web page we want to scrape.')
@click.option('--length', help = "length of the output from wikipedia")
def cli(name,length):
    result =scrape(name, length = length)
    click.echo(click.style(f"{result}", fg = "blue"))

if __name__ == '__main__':
    cli()
