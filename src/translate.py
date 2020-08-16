import boto3

client = boto3.client('translate', region_name="us-west-2")
text = "我的名字叫王鑫"
result = client.translate_text(Text=text, SourceLanguageCode="auto", TargetLanguageCode="en")
print(result['TranslatedText'])