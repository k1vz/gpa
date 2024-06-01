# Generated by Django 3.2.19 on 2024-06-01 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=255)),
                ('inadimplente', models.BooleanField(default=False)),
                ('tipo_cliente', models.CharField(choices=[('PJ', 'Pessoa Jurídica'), ('PF', 'Pessoa Física')], max_length=2)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('cnpj', models.CharField(blank=True, max_length=18, null=True, unique=True)),
                ('dataNascimento', models.DateField()),
                ('inscricaoEstadual', models.CharField(max_length=9)),
                ('qntCaminhoes', models.IntegerField()),
                ('razaoSocial', models.CharField(max_length=100)),
                ('nomeFantasia', models.CharField(max_length=100)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_modificacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=255)),
                ('numero', models.IntegerField()),
                ('municipio', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('ponto_referencia', models.CharField(blank=True, max_length=255, null=True)),
                ('bairro', models.CharField(max_length=100)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to='clientes.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('telefone', models.CharField(max_length=50)),
                ('telefone_secundario', models.CharField(blank=True, max_length=50, null=True)),
                ('cargo', models.CharField(blank=True, max_length=50, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contatos', to='clientes.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='clientes.contato'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='clientes.endereco'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='usuarios.usuario'),
        ),
    ]
