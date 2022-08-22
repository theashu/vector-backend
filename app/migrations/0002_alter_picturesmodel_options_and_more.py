from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picturesmodel',
            options={'ordering': ('position',), 'verbose_name_plural': 'Picture Detail'},
        ),
        migrations.AlterField(
            model_name='picturesmodel',
            name='position',
            field=models.IntegerField(unique=True, verbose_name='Postion'),
        ),
    ]