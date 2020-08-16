import boto3
import click
@click.command()
@click.option('--phrase', prompt=' put in pharse in any language to translate', help='this is a tool that translate text')
def action(phrase):
    client = boto3.client('translate', region_name="us-west-2")
    click.echo(click.style(f"Translate phrase: {phrase}",fg='red'))
    result = client.translate_text(Text=phrase, SourceLanguageCode="auto", TargetLanguageCode="en")
    text = result['TranslatedText']
    click.echo(click.style(f'{text}',bg='blue',fg='white'))

if __name__=='__main__':
    action()
