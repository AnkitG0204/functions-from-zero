import wikipedia

def scrape(name = "Microsoft",length=1 ):
    result = wikipedia.summary(name, sentences = length)
    return result
    click.echo(click.style(f"{result}", fg = "blue"))