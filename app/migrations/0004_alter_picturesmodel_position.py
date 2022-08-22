from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_picturesmodel_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturesmodel',
            name='position',
            field=models.IntegerField(verbose_name='Position'),
        ),
    ]