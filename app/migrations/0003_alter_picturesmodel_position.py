from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_picturesmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturesmodel',
            name='position',
            field=models.IntegerField(unique=True, verbose_name='Position'),
        ),
    ]