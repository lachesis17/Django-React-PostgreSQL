# Generated by Django 5.1.1 on 2024-10-08 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_cong_csq_cong_cong_sq_alter_grag_file_fset_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CORE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CORE_TOP', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Top of Core Run')),
                ('CORE_BASE', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Base of Core Run')),
                ('CORE_PREC', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Percentage of Core Recovered in Core Run')),
                ('CORE_SREC', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Percentage of Solid Core Recovered in Core Run')),
                ('CORE_RQD', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Rock Quality Designation for Core Run')),
                ('CORE_DIAM', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Core Diameter')),
                ('CORE_DURN', models.TimeField(verbose_name='Time Taken to Drill Core Run')),
                ('CORE_REM', models.TextField(verbose_name='Remarks')),
                ('FILE_FSET', models.CharField(max_length=255, verbose_name='File Reference')),
                ('LOCA_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coring', to='core.loca', verbose_name='Location')),
            ],
        ),
        migrations.CreateModel(
            name='RCAG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOCA_ID', models.CharField(blank=True, max_length=255, verbose_name='Location')),
                ('SAMP_TOP', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Top of Sample')),
                ('SAMP_REF', models.CharField(blank=True, max_length=255, verbose_name='Sample Reference')),
                ('SAMP_TYPE', models.CharField(blank=True, max_length=255, verbose_name='Sample Type')),
                ('SPEC_REF', models.CharField(blank=True, max_length=255, verbose_name='Specimen Reference')),
                ('SPEC_DPTH', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Top of Test Specimen')),
                ('SPEC_DESC', models.TextField(blank=True, verbose_name='Specimen Description')),
                ('SPEC_PREP', models.TextField(blank=True, verbose_name='Details of Specimen Preparation')),
                ('SPEC_BASE', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Base of Specimen')),
                ('RCAG_DEV', models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')),
                ('RCAG_DATE', models.DateField(verbose_name='Date of Test')),
                ('RCAG_COND', models.CharField(blank=True, max_length=255, verbose_name='Condition of Specimen as Tested')),
                ('RCAG_GSIZ', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Maximum Grain Size')),
                ('RCAG_ANIS', models.CharField(blank=True, max_length=255, verbose_name='Planes of Weakness or Anisotropy Present')),
                ('RCAG_MACH', models.CharField(blank=True, max_length=255, verbose_name='Type of Apparatus')),
                ('RCAG_MMTD', models.CharField(blank=True, max_length=255, verbose_name='Measurement Method')),
                ('RCAG_CAIM', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='CAI Mean Value')),
                ('RCAG_CAIS', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='CAI Standard Deviation')),
                ('RCAG_ABCL', models.CharField(blank=True, max_length=255, verbose_name='Abrasiveness Classification')),
                ('RCAG_REM', models.TextField(blank=True, verbose_name='Remarks')),
                ('RCAG_METH', models.CharField(blank=True, max_length=255, verbose_name='Test Method')),
                ('RCAG_LAB', models.CharField(blank=True, max_length=255, verbose_name='Name of Testing Laboratory/Organization')),
                ('RCAG_CRED', models.CharField(blank=True, max_length=255, verbose_name='Accrediting Body and Reference Number')),
                ('TEST_STAT', models.CharField(blank=True, max_length=255, verbose_name='Test Status')),
                ('FILE_FSET', models.CharField(blank=True, max_length=255, verbose_name='File Reference')),
                ('SAMP_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rock_abrasive_general', to='core.samp', verbose_name='Sample ID')),
            ],
        ),
        migrations.CreateModel(
            name='RCAT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOCA_ID', models.CharField(blank=True, max_length=255, verbose_name='Location')),
                ('SAMP_TOP', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Top of Sample')),
                ('SAMP_REF', models.CharField(blank=True, max_length=255, verbose_name='Sample Reference')),
                ('SAMP_TYPE', models.CharField(blank=True, max_length=255, verbose_name='Sample Type')),
                ('SPEC_REF', models.CharField(blank=True, max_length=255, verbose_name='Specimen Reference')),
                ('SPEC_DPTH', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Top of Test Specimen')),
                ('RCAT_TESN', models.CharField(blank=True, max_length=255, verbose_name='Measurement Number')),
                ('RCAT_CUT', models.CharField(blank=True, max_length=255, verbose_name='Surface Condition')),
                ('RCAT_SDIR', models.CharField(blank=True, max_length=255, verbose_name='Direction of Scratching')),
                ('RCAT_STYH', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Rockwell Hardness HRC of Stylus')),
                ('RCAT_STYC', models.CharField(blank=True, max_length=255, verbose_name='Stylus Condition')),
                ('RCAT_CAI', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='As Measured CAI Value')),
                ('RCAT_CAIS', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Equivalent CAI Value')),
                ('RCAT_REM', models.TextField(blank=True, verbose_name='Remarks')),
                ('FILE_FSET', models.CharField(blank=True, max_length=255, verbose_name='File Reference')),
                ('SAMP_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rock_abrasive_test', to='core.rcag', verbose_name='Sample ID')),
            ],
        ),
        migrations.CreateModel(
            name='RCCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOCA_ID', models.CharField(max_length=255, verbose_name='Location')),
                ('SAMP_TOP', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Top of Sample')),
                ('SAMP_REF', models.CharField(max_length=255, verbose_name='Sample Reference')),
                ('SAMP_TYPE', models.CharField(max_length=255, verbose_name='Sample Type')),
                ('SPEC_REF', models.CharField(max_length=255, verbose_name='Specimen Reference')),
                ('SPEC_DPTH', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Top of Test Specimen')),
                ('SPEC_DESC', models.TextField(verbose_name='Specimen Description')),
                ('SPEC_PREP', models.TextField(verbose_name='Details of Specimen Preparation')),
                ('RCCV_MC', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Water Content of Specimen Tested')),
                ('RCCV_CCV', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Chalk Crushing Value')),
                ('RCCV_100', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Percentage Larger Than 10mm in Original Sample')),
                ('RCCV_REM', models.TextField(verbose_name='Remarks')),
                ('RCCV_METH', models.CharField(max_length=255, verbose_name='Test Method')),
                ('RCCV_LAB', models.CharField(max_length=255, verbose_name='Name of Testing Laboratory/Organization')),
                ('RCCV_CRED', models.CharField(max_length=255, verbose_name='Accrediting Body and Reference Number')),
                ('TEST_STAT', models.CharField(max_length=255, verbose_name='Test Status')),
                ('FILE_FSET', models.CharField(max_length=255, verbose_name='File Reference')),
                ('SPEC_BASE', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Base of Specimen')),
                ('RCCV_DEV', models.TextField(verbose_name='Deviation from the Specified Procedure')),
                ('SAMP_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chalk_crush', to='core.samp', verbose_name='Sample ID')),
            ],
        ),
        migrations.CreateModel(
            name='RDEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOCA_ID', models.CharField(blank=True, max_length=255, verbose_name='Location')),
                ('SAMP_TOP', models.FloatField(null=True, verbose_name='Depth to Top of Sample')),
                ('SAMP_REF', models.CharField(blank=True, max_length=255, verbose_name='Sample Reference')),
                ('SAMP_TYPE', models.CharField(blank=True, max_length=255, verbose_name='Sample Type')),
                ('SPEC_REF', models.CharField(blank=True, max_length=255, verbose_name='Specimen Reference')),
                ('SPEC_DPTH', models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')),
                ('SPEC_DESC', models.TextField(blank=True, verbose_name='Specimen Description')),
                ('SPEC_PREP', models.TextField(blank=True, verbose_name='Details of Specimen Preparation')),
                ('RDEN_MC', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Water Content of Specimen')),
                ('RDEN_SMC', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Saturated Water Content')),
                ('RDEN_BDEN', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Bulk Density')),
                ('RDEN_DDEN', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Dry Density')),
                ('RDEN_PORO', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Porosity')),
                ('RDEN_PDEN', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Apparent Particle Density')),
                ('RDEN_TEMP', models.IntegerField(null=True, verbose_name='Temperature Sample Dried At')),
                ('RDEN_REM', models.TextField(blank=True, verbose_name='Remarks')),
                ('RDEN_METH', models.CharField(blank=True, max_length=255, verbose_name='Test Method')),
                ('RDEN_LAB', models.CharField(blank=True, max_length=255, verbose_name='Name of Testing Laboratory/Organization')),
                ('RDEN_CRED', models.CharField(blank=True, max_length=255, verbose_name='Accrediting Body and Reference Number')),
                ('TEST_STAT', models.CharField(blank=True, max_length=255, verbose_name='Test Status')),
                ('FILE_FSET', models.CharField(blank=True, max_length=255, verbose_name='File Reference')),
                ('RDEN_IDEN', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Intact Dry Density')),
                ('SPEC_BASE', models.FloatField(null=True, verbose_name='Depth to Base of Specimen')),
                ('RDEN_DEV', models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')),
                ('SAMP_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rock_density', to='core.samp', verbose_name='Sample ID')),
            ],
        ),
        migrations.CreateModel(
            name='RPLT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOCA_ID', models.CharField(max_length=255, verbose_name='Location')),
                ('SAMP_TOP', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Top of Sample')),
                ('SAMP_REF', models.CharField(max_length=255, verbose_name='Sample Reference')),
                ('SAMP_TYPE', models.CharField(max_length=255, verbose_name='Sample Type')),
                ('SPEC_REF', models.CharField(max_length=255, verbose_name='Specimen Reference')),
                ('SPEC_DPTH', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Top of Test Specimen')),
                ('SPEC_DESC', models.TextField(verbose_name='Specimen Description')),
                ('SPEC_PREP', models.TextField(verbose_name='Details of Specimen Preparation')),
                ('RPLT_PLS', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Uncorrected Point Load (Is)')),
                ('RPLT_PLSI', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Size Corrected Point Load Index (Is 50)')),
                ('RPLT_PLTF', models.CharField(max_length=255, verbose_name='Point Load Test Type')),
                ('RPLT_MC', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Water Content of Point Load Test Specimen')),
                ('RPLT_REM', models.TextField(verbose_name='Remarks')),
                ('RPLT_METH', models.CharField(max_length=255, verbose_name='Test Method')),
                ('RPLT_LAB', models.CharField(max_length=255, verbose_name='Name of Testing Laboratory/Organization')),
                ('RPLT_CRED', models.CharField(max_length=255, verbose_name='Accrediting Body and Reference Number')),
                ('TEST_STAT', models.CharField(max_length=255, verbose_name='Test Status')),
                ('FILE_FSET', models.CharField(max_length=255, verbose_name='File Reference')),
                ('SPEC_BASE', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Base of Specimen')),
                ('RPLT_DEV', models.TextField(verbose_name='Deviation from the Specified Procedure')),
                ('SAMP_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='point_load', to='core.samp', verbose_name='Sample ID')),
            ],
        ),
        migrations.CreateModel(
            name='RTEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOCA_ID', models.CharField(max_length=255, verbose_name='Location')),
                ('SAMP_TOP', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Top of Sample')),
                ('SAMP_REF', models.CharField(max_length=255, verbose_name='Sample Reference')),
                ('SAMP_TYPE', models.CharField(max_length=255, verbose_name='Sample Type')),
                ('SPEC_REF', models.CharField(max_length=255, verbose_name='Specimen Reference')),
                ('SPEC_DPTH', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Top of Test Specimen')),
                ('SPEC_DESC', models.TextField(verbose_name='Specimen Description')),
                ('SPEC_PREP', models.TextField(verbose_name='Details of Specimen Preparation')),
                ('RTEN_SDIA', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Specimen Diameter')),
                ('RTEN_LEN', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Specimen Thickness')),
                ('RTEN_MC', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Water Content of Test Specimen')),
                ('RTEN_COND', models.CharField(max_length=255, verbose_name='Condition of Specimen as Tested')),
                ('RTEN_DURN', models.DurationField(verbose_name='Test Duration')),
                ('RTEN_STRA', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Stress Rate')),
                ('RTEN_TENS', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Tensile Strength')),
                ('RTEN_MODE', models.CharField(max_length=255, verbose_name='Mode of Failure')),
                ('RTEN_MACH', models.CharField(max_length=255, verbose_name='Testing Machine')),
                ('RTEN_REM', models.TextField(verbose_name='Remarks')),
                ('RTEN_METH', models.CharField(max_length=255, verbose_name='Test Method')),
                ('RTEN_LAB', models.CharField(max_length=255, verbose_name='Name of Testing Laboratory/Organization')),
                ('RTEN_CRED', models.CharField(max_length=255, verbose_name='Accrediting Body and Reference Number')),
                ('TEST_STAT', models.CharField(max_length=255, verbose_name='Test Status')),
                ('FILE_FSET', models.CharField(max_length=255, verbose_name='File Reference')),
                ('SPEC_BASE', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Depth to Base of Specimen')),
                ('RTEN_DEV', models.TextField(verbose_name='Deviation from the Specified Procedure')),
                ('SAMP_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rock_tensile', to='core.samp', verbose_name='Sample ID')),
            ],
        ),
        migrations.CreateModel(
            name='RUCS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOCA_ID', models.CharField(blank=True, max_length=255, verbose_name='Location')),
                ('SAMP_TOP', models.FloatField(null=True, verbose_name='Depth to Top of Sample')),
                ('SAMP_REF', models.CharField(blank=True, max_length=255, verbose_name='Sample Reference')),
                ('SAMP_TYPE', models.CharField(blank=True, max_length=255, verbose_name='Sample Type')),
                ('SPEC_REF', models.CharField(blank=True, max_length=255, verbose_name='Specimen Reference')),
                ('SPEC_DPTH', models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')),
                ('SPEC_DESC', models.TextField(blank=True, verbose_name='Specimen Description')),
                ('SPEC_PREP', models.TextField(blank=True, verbose_name='Details of Specimen Preparation')),
                ('RUCS_SDIA', models.FloatField(null=True, verbose_name='Specimen Diameter')),
                ('RUCS_LEN', models.FloatField(null=True, verbose_name='Specimen Length')),
                ('RUCS_MC', models.FloatField(null=True, verbose_name='Water Content of Specimen Tested')),
                ('RUCS_COND', models.CharField(blank=True, max_length=255, verbose_name='Condition of Specimen as Tested')),
                ('RUCS_DURN', models.CharField(blank=True, max_length=255, verbose_name='Test Duration')),
                ('RUCS_STRA', models.FloatField(null=True, verbose_name='Stress Rate')),
                ('RUCS_UCS', models.FloatField(null=True, verbose_name='Uniaxial Compressive Strength')),
                ('RUCS_MODE', models.CharField(blank=True, max_length=255, verbose_name='Mode of Failure')),
                ('RUCS_E', models.FloatField(null=True, verbose_name="Young's Modulus")),
                ('RUCS_MU', models.FloatField(null=True, verbose_name="Poisson's Ratio")),
                ('RUCS_ES', models.CharField(blank=True, max_length=255, verbose_name='Stress Level at Which Modulus Has Been Measured')),
                ('RUCS_METH', models.CharField(blank=True, max_length=255, verbose_name='Test Method')),
                ('RUCS_LAB', models.CharField(blank=True, max_length=255, verbose_name='Name of Testing Laboratory/Organization')),
                ('RUCS_CRED', models.CharField(blank=True, max_length=255, verbose_name='Accrediting Body and Reference Number')),
                ('TEST_STAT', models.CharField(blank=True, max_length=255, verbose_name='Test Status')),
                ('FILE_FSET', models.CharField(blank=True, max_length=255, verbose_name='File Reference')),
                ('SPEC_BASE', models.FloatField(null=True, verbose_name='Depth to Base of Specimen')),
                ('RUCS_DEV', models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')),
                ('RUCS_REM', models.TextField(blank=True, verbose_name='Remarks')),
                ('RUCS_MACH', models.CharField(blank=True, max_length=255, verbose_name='Type of Testing Machine')),
                ('RUCS_ESEC', models.FloatField(null=True, verbose_name="Young's Modulus, Secant")),
                ('RUCS_ETAN', models.FloatField(null=True, verbose_name="Young's Modulus, Tangent")),
                ('RUCS_EAVG', models.FloatField(null=True, verbose_name="Young's Modulus, Average")),
                ('RUCS_SSEC', models.CharField(blank=True, max_length=255, verbose_name="Stress Level at Which Secant Young's Modulus Has Been Measured")),
                ('RUCS_STAN', models.CharField(blank=True, max_length=255, verbose_name="Stress Level at Which Tangent Young's Modulus Has Been Measured")),
                ('RUCS_SAVG', models.CharField(blank=True, max_length=255, verbose_name="Stress Level at Which Average Young's Modulus Has Been Measured")),
                ('RUCS_MUS', models.FloatField(null=True, verbose_name="Poisson's Ratio, Secant")),
                ('RUCS_MUT', models.FloatField(null=True, verbose_name="Poisson's Ratio, Tangent")),
                ('RUCS_MUAV', models.FloatField(null=True, verbose_name="Poisson's Ratio, Average")),
                ('SAMP_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ucs', to='core.samp', verbose_name='Sample ID')),
            ],
        ),
        migrations.CreateModel(
            name='RWCO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOCA_ID', models.CharField(blank=True, max_length=255, verbose_name='Location')),
                ('SAMP_TOP', models.FloatField(null=True, verbose_name='Depth to Top of Sample')),
                ('SAMP_REF', models.CharField(blank=True, max_length=255, verbose_name='Sample Reference')),
                ('SAMP_TYPE', models.CharField(blank=True, max_length=255, verbose_name='Sample Type')),
                ('SPEC_REF', models.CharField(blank=True, max_length=255, verbose_name='Specimen Reference')),
                ('SPEC_DPTH', models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')),
                ('SPEC_DESC', models.TextField(blank=True, verbose_name='Specimen Description')),
                ('SPEC_PREP', models.TextField(blank=True, verbose_name='Details of Specimen Preparation')),
                ('RWCO_MC', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Water Content')),
                ('RWCO_TEMP', models.IntegerField(null=True, verbose_name='Temperature Sample Dried At')),
                ('RWCO_REM', models.TextField(blank=True, verbose_name='Remarks')),
                ('RWCO_METH', models.CharField(blank=True, max_length=255, verbose_name='Test Method')),
                ('RWCO_LAB', models.CharField(blank=True, max_length=255, verbose_name='Name of Testing Laboratory/Organization')),
                ('RWCO_CRED', models.CharField(blank=True, max_length=255, verbose_name='Accrediting Body and Reference Number')),
                ('TEST_STAT', models.CharField(blank=True, max_length=255, verbose_name='Test Status')),
                ('FILE_FSET', models.CharField(blank=True, max_length=255, verbose_name='File Reference')),
                ('SPEC_BASE', models.FloatField(null=True, verbose_name='Depth to Base of Specimen')),
                ('RWCO_DEV', models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')),
                ('SAMP_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rock_moisture', to='core.samp', verbose_name='Sample ID')),
            ],
        ),
    ]
