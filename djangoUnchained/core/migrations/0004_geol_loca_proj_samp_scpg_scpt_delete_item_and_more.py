# Generated by Django 5.1.1 on 2024-10-07 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cptdata_u_alter_cptdata_fs_alter_cptdata_qc'),
    ]

    operations = [
        migrations.CreateModel(
            name='GEOL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GEOL_TOP', models.FloatField(verbose_name='Depth to the Top of Stratum (m)')),
                ('GEOL_BASE', models.FloatField(verbose_name='Depth to the Base of Description (m)')),
                ('GEOL_DESC', models.TextField(blank=True, verbose_name='General Description of Stratum')),
                ('GEOL_LEG', models.CharField(max_length=50, verbose_name='Legend Code (Soil Type)')),
                ('GEOL_GEOL', models.CharField(blank=True, max_length=50, verbose_name='Geology Code (Soil Unit)')),
                ('GEOL_GEO2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Second Geology Code (Soil Unit)')),
                ('GEOL_STAT', models.CharField(blank=True, max_length=50, null=True, verbose_name='Stratum Reference Shown on Trial Pit or Traverse Sketch')),
                ('GEOL_BGS', models.CharField(blank=True, max_length=50, null=True, verbose_name='BGS Lexicon Code')),
                ('GEOL_FORM', models.CharField(blank=True, max_length=255, null=True, verbose_name='Geological Formation or Stratum Name')),
                ('GEOL_REM', models.TextField(blank=True, null=True, verbose_name='Remarks')),
                ('FILE_FSET', models.CharField(blank=True, max_length=255, null=True, verbose_name='Associated File Reference (e.g., logging field sheets, photographs of exposures)')),
            ],
        ),
        migrations.CreateModel(
            name='LOCA',
            fields=[
                ('LOCA_ID', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Location Identifier')),
                ('LOCA_TYPE', models.CharField(blank=True, max_length=50, verbose_name='Type of Activity')),
                ('LOCA_STAT', models.CharField(blank=True, max_length=50, verbose_name='Status of Information Relating to this Position')),
                ('LOCA_NATE', models.FloatField(null=True, verbose_name='National Grid Easting of Location or Start of Traverse')),
                ('LOCA_NATN', models.FloatField(null=True, verbose_name='National Grid Northing of Location or Start of Traverse')),
                ('LOCA_GREF', models.CharField(blank=True, max_length=50, verbose_name='National Grid Referencing System Used')),
                ('LOCA_GL', models.FloatField(null=True, verbose_name='Ground Level Relative to Datum of Location or Start of Traverse')),
                ('LOCA_REM', models.TextField(blank=True, max_length=255, verbose_name='General Remarks')),
                ('LOCA_FDEP', models.FloatField(verbose_name='Final Depth')),
                ('LOCA_STAR', models.DateTimeField(blank=True, verbose_name='Date of Start of Activity')),
                ('LOCA_PURP', models.CharField(blank=True, max_length=255, verbose_name='Purpose of Activity at this Location')),
                ('LOCA_TERM', models.CharField(blank=True, max_length=255, verbose_name='Reason for Activity Termination')),
                ('LOCA_ENDD', models.DateTimeField(blank=True, verbose_name='End Date of Activity')),
                ('LOCA_LETT', models.CharField(blank=True, max_length=50, verbose_name='OSGB Letter Grid Reference')),
                ('LOCA_LOCX', models.FloatField(null=True, verbose_name='Local Grid X Coordinate or Start of Traverse')),
                ('LOCA_LOCY', models.FloatField(null=True, verbose_name='Local Grid Y Coordinate or Start of Traverse')),
                ('LOCA_LOCZ', models.FloatField(null=True, verbose_name='Level or Start of Traverse to Local Datum')),
                ('LOCA_LREF', models.CharField(blank=True, max_length=50, verbose_name='Local Grid Referencing System Used')),
                ('LOCA_DATM', models.CharField(blank=True, max_length=50, verbose_name='Local Datum Referencing System Used')),
                ('LOCA_ETRV', models.FloatField(null=True, verbose_name='National Grid Easting of End of Traverse')),
                ('LOCA_NTRV', models.FloatField(null=True, verbose_name='National Grid Northing of End of Traverse')),
                ('LOCA_LTRV', models.FloatField(null=True, verbose_name='Ground Level Relative to Datum of End of Traverse')),
                ('LOCA_XTRL', models.FloatField(null=True, verbose_name='Local Grid Easting of End of Traverse')),
                ('LOCA_YTRL', models.FloatField(null=True, verbose_name='Local Grid Northing of End of Traverse')),
                ('LOCA_ZTRL', models.FloatField(null=True, verbose_name='Local Elevation of End of Traverse')),
                ('LOCA_LAT', models.CharField(blank=True, max_length=50, verbose_name='Latitude of Location or Start of Traverse')),
                ('LOCA_LON', models.CharField(blank=True, max_length=50, verbose_name='Longitude of Location or Start of Traverse')),
                ('LOCA_ELAT', models.CharField(blank=True, max_length=50, verbose_name='Latitude of End of Traverse')),
                ('LOCA_ELON', models.CharField(blank=True, max_length=50, verbose_name='Longitude of End of Traverse')),
                ('LOCA_LLIZ', models.CharField(blank=True, max_length=50, verbose_name='Projection Format')),
                ('LOCA_LOCM', models.CharField(blank=True, max_length=50, verbose_name='Method of Location')),
                ('LOCA_LOCA', models.CharField(blank=True, max_length=50, verbose_name='Site Location Sub Division (within Project)')),
                ('LOCA_CLST', models.CharField(blank=True, max_length=50, verbose_name='Investigation Phase Grouping Code or Description')),
                ('LOCA_ALID', models.CharField(blank=True, max_length=50, verbose_name='Alignment Identifier')),
                ('LOCA_OFFS', models.FloatField(null=True, verbose_name='Offset')),
                ('LOCA_CNGE', models.CharField(blank=True, max_length=50, verbose_name='Chainage')),
                ('LOCA_TRAN', models.TextField(blank=True, verbose_name='Details of Algorithm Used to Calculate Local Grid Reference')),
                ('FILE_FSET', models.CharField(blank=True, max_length=255, verbose_name='File Reference')),
                ('LOCA_NATD', models.CharField(blank=True, max_length=50, verbose_name='National Datum Referencing System Used')),
                ('LOCA_ORID', models.CharField(blank=True, max_length=50, verbose_name='Original Hole ID')),
                ('LOCA_ORJO', models.CharField(blank=True, max_length=50, verbose_name='Original Job Reference')),
                ('LOCA_ORCO', models.CharField(blank=True, max_length=50, verbose_name='Originating Company')),
            ],
        ),
        migrations.CreateModel(
            name='PROJ',
            fields=[
                ('PROJ_ID', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Project Identifier')),
                ('PROJ_NAME', models.CharField(max_length=255, verbose_name='Name')),
                ('PROJ_LOC', models.CharField(max_length=255, verbose_name='Location')),
                ('PROJ_CLNT', models.CharField(blank=True, max_length=255, verbose_name='Client')),
                ('PROJ_CONT', models.CharField(blank=True, max_length=255, verbose_name='Contractor')),
                ('PROJ_ENG', models.CharField(blank=True, max_length=255, verbose_name='Project Engineer')),
                ('PROJ_MEMO', models.TextField(blank=True, verbose_name='Remarks')),
                ('FILE_FSET', models.CharField(blank=True, max_length=255, verbose_name='File Reference')),
            ],
        ),
        migrations.CreateModel(
            name='SAMP',
            fields=[
                ('SAMP_TOP', models.FloatField(verbose_name='Depth to Top of Sample')),
                ('SAMP_REF', models.CharField(max_length=50, verbose_name='Sample Reference')),
                ('SAMP_TYPE', models.CharField(max_length=50, verbose_name='Sample Type')),
                ('SAMP_ID', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Sample Unique Identifier')),
                ('SAMP_BASE', models.FloatField(null=True, verbose_name='Depth to Base of Sample')),
                ('SAMP_DTIM', models.DateTimeField(blank=True, verbose_name='Date and Time Sample Taken')),
                ('SAMP_UBLO', models.IntegerField(null=True, verbose_name='Number of Blows Required to Drive Sampler')),
                ('SAMP_CONT', models.CharField(blank=True, max_length=255, verbose_name='Sample Container')),
                ('SAMP_PREP', models.CharField(blank=True, max_length=255, verbose_name='Details of Sample Preparation at Time of Sampling')),
                ('SAMP_SDIA', models.FloatField(null=True, verbose_name='Sample Diameter')),
                ('SAMP_WDEP', models.FloatField(null=True, verbose_name='Depth to Water Below Ground Surface at Time of Sampling')),
                ('SAMP_RECV', models.FloatField(null=True, verbose_name='Percentage of Sample Recovered')),
                ('SAMP_TECH', models.CharField(blank=True, max_length=50, verbose_name='Sampling Technique/Method')),
                ('SAMP_MATX', models.CharField(blank=True, max_length=50, verbose_name='Sample Matrix')),
                ('SAMP_TYPC', models.CharField(blank=True, max_length=50, verbose_name='Sample QA Type (Normal, Blank or Spike)')),
                ('SAMP_WHO', models.CharField(blank=True, max_length=50, verbose_name='Samplers Initials or Name')),
                ('SAMP_WHY', models.CharField(blank=True, max_length=255, verbose_name='Reason for Sampling')),
                ('SAMP_REM', models.TextField(blank=True, verbose_name='Sample Remarks')),
                ('SAMP_DESC', models.CharField(blank=True, max_length=255, verbose_name='Sample/Specimen Description')),
                ('SAMP_DESD', models.DateField(blank=True, verbose_name='Date Sample Described')),
                ('SAMP_LOG', models.CharField(blank=True, max_length=50, verbose_name='Person Responsible for Sample/Specimen Description')),
                ('SAMP_COND', models.CharField(blank=True, max_length=255, verbose_name='Condition and Representativeness of Sample')),
                ('SAMP_CLSS', models.CharField(blank=True, max_length=50, verbose_name='Sample Classification as Required by EN ISO 14688-1')),
                ('SAMP_BAR', models.FloatField(null=True, verbose_name='Barometric Pressure at Time of Sampling')),
                ('SAMP_TEMP', models.FloatField(null=True, verbose_name='Sample Temperature at Time of Sampling')),
                ('SAMP_PRES', models.FloatField(null=True, verbose_name='Gas Pressure (Above Barometric)')),
                ('SAMP_FLOW', models.FloatField(null=True, verbose_name='Gas Flow Rate')),
                ('SAMP_ETIM', models.DateTimeField(null=True, verbose_name='Date and Time Sampling Completed')),
                ('SAMP_DURN', models.TimeField(blank=True, verbose_name='Sampling Duration')),
                ('SAMP_CAPT', models.CharField(blank=True, max_length=255, verbose_name='Caption Used to Describe Sample')),
                ('SAMP_LINK', models.CharField(blank=True, max_length=255, verbose_name='Sample Record Link')),
                ('GEOL_STAT', models.CharField(blank=True, max_length=50, verbose_name='Stratum Reference Shown on Trial Pit or Traverse Sketch')),
                ('FILE_FSET', models.CharField(blank=True, max_length=255, verbose_name='File Reference (SSDS)')),
                ('SAMP_RECL', models.FloatField(null=True, verbose_name='Length of Sample Recovered')),
            ],
        ),
        migrations.CreateModel(
            name='SCPG',
            fields=[
                ('SCPG_TESN', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Test Reference or Push Number')),
                ('SCPG_DEPTH', models.FloatField(verbose_name='Top Depth of Cone Push')),
                ('SCPG_TYPE', models.CharField(blank=True, max_length=50, verbose_name='Cone Test Type')),
                ('SCPG_REF', models.CharField(blank=True, max_length=50, verbose_name='Cone Reference')),
                ('SCPG_CSA', models.FloatField(null=True, verbose_name='Surface Area of Cone Tip')),
                ('SCPG_RATE', models.FloatField(null=True, verbose_name='Nominal Rate of Penetration of the Cone')),
                ('SCPG_FILT', models.CharField(blank=True, max_length=50, verbose_name='Type of Filter Material Used')),
                ('SCPG_FRIC', models.CharField(blank=True, max_length=2, verbose_name='Friction Reducer Used')),
                ('SCPG_WAT', models.FloatField(null=True, verbose_name='Groundwater Level at Time of Test')),
                ('SCPG_WATA', models.CharField(blank=True, max_length=255, verbose_name='Origin of Water Level in SCPG_WAT')),
                ('SCPG_REM', models.TextField(blank=True, verbose_name='Comments on Testing and Basis of Any Interpreted Parameters Included in SCPT and SCPP')),
                ('SCPG_ENV', models.CharField(blank=True, max_length=255, verbose_name='Details of Weather and Environmental Conditions During Test')),
                ('SCPG_CONT', models.CharField(blank=True, max_length=255, verbose_name='Subcontractors Name')),
                ('SCPG_METH', models.CharField(blank=True, max_length=50, verbose_name='Standard Followed for Testing')),
                ('SCPG_CRED', models.CharField(blank=True, max_length=255, verbose_name='Accrediting Body and Reference Number')),
                ('SCPG_CAR', models.FloatField(null=True, verbose_name='Cone Area Ratio Used to Calculate qt')),
                ('SCPG_SLAR', models.FloatField(null=True, verbose_name='Sleeve Area Ratio Used to Calculate ft')),
                ('FILE_FSET', models.CharField(blank=True, max_length=255, verbose_name='File Reference (Cone Certificates)')),
            ],
        ),
        migrations.CreateModel(
            name='SCPT',
            fields=[
                ('SCPT_DPTH', models.FloatField(primary_key=True, serialize=False, verbose_name='Depth of Result (m)')),
                ('SCPT_RES', models.FloatField(verbose_name='Cone Resistance (qc) (MPa)')),
                ('SCPT_FRES', models.FloatField(verbose_name='Local Unit Side Friction Resistance (fs) (MPa)')),
                ('SCPT_PWP1', models.FloatField(verbose_name='Face Porewater Pressure (u1) (kPa)')),
                ('SCPT_PWP2', models.FloatField(null=True, verbose_name='Shoulder Porewater Pressure (u2) (kPa)')),
                ('SCPT_PWP3', models.FloatField(null=True, verbose_name='Top of Sleeve Porewater Pressure (u3) (kPa)')),
                ('SCPT_CON', models.FloatField(null=True, verbose_name='Conductivity (us/cm)')),
                ('SCPT_TEMP', models.FloatField(null=True, verbose_name='Temperature (°C)')),
                ('SCPT_PH', models.FloatField(null=True, verbose_name='pH Reading')),
                ('SCPT_SLP1', models.FloatField(null=True, verbose_name='Slope Indicator No. 1 (deg)')),
                ('SCPT_SLP2', models.FloatField(null=True, verbose_name='Slope Indicator No. 2 (deg)')),
                ('SCPT_REDX', models.FloatField(null=True, verbose_name='Redox Potential Reading (mV)')),
                ('SCPT_MAGT', models.FloatField(null=True, verbose_name='Magnetic Flux - Total (nT)')),
                ('SCPT_MAGX', models.FloatField(null=True, verbose_name='Magnetic Flux - X (nT)')),
                ('SCPT_MAGY', models.FloatField(null=True, verbose_name='Magnetic Flux - Y (nT)')),
                ('SCPT_MAGZ', models.FloatField(null=True, verbose_name='Magnetic Flux - Z (nT)')),
                ('SCPT_SMP', models.FloatField(null=True, verbose_name='Soil Moisture (%)')),
                ('SCPT_NGAM', models.FloatField(null=True, verbose_name='Natural Gamma Radiation (counts/s)')),
                ('SCPT_REM', models.TextField(verbose_name='Remarks')),
                ('SCPT_FRR', models.FloatField(null=True, verbose_name='Friction Ratio (Rf) (%)')),
                ('SCPT_QT', models.FloatField(null=True, verbose_name='Corrected Cone Resistance (qt) (MPa)')),
                ('SCPT_FT', models.FloatField(null=True, verbose_name='Corrected Sleeve Resistance (ft) (MPa)')),
                ('SCPT_QE', models.FloatField(null=True, verbose_name='Effective Cone Resistance (qe) (MPa)')),
                ('SCPT_BDEN', models.FloatField(null=True, verbose_name='Bulk Density of Material (Mg/m3)')),
                ('SCPT_CPO', models.FloatField(null=True, verbose_name='Total Vertical Stress (kPa)')),
                ('SCPT_CPOD', models.FloatField(null=True, verbose_name='Effective Vertical Stress (kPa)')),
                ('SCPT_QNET', models.FloatField(null=True, verbose_name='Net Cone Resistance (qn) (MPa)')),
                ('SCPT_FRRC', models.FloatField(null=True, verbose_name='Corrected Friction Ratio (Rf) (%)')),
                ('SCPT_EXPP', models.FloatField(null=True, verbose_name='Excess Pore Pressure (u-u0) (MPa)')),
                ('SCPT_BQ', models.FloatField(null=True, verbose_name='Pore Pressure Ratio (Bq)')),
                ('SCPT_ISPP', models.FloatField(null=True, verbose_name='In Situ Pore Pressure (u0) (MPa)')),
                ('SCPT_NQT', models.FloatField(null=True, verbose_name='Normalised Cone Resistance (Qt)')),
                ('SCPT_NFR', models.FloatField(null=True, verbose_name='Normalised Friction Ratio (Fr) (%)')),
                ('FILE_FSET', models.CharField(max_length=255, verbose_name='File Reference (Raw Field Data)')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='geol',
            name='LOCA_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='geological_descriptions', to='core.loca', verbose_name='Location Identifier'),
        ),
        migrations.AddField(
            model_name='loca',
            name='PROJ_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='core.proj', verbose_name='Project Identifier'),
        ),
        migrations.AddField(
            model_name='samp',
            name='LOCA_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='core.loca'),
        ),
        migrations.AddField(
            model_name='scpg',
            name='LOCA_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cone_penetration_tests', to='core.loca'),
        ),
        migrations.AddField(
            model_name='scpt',
            name='SCPG_TESN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cone_id', to='core.scpg', verbose_name='Test Reference or Push Number'),
        ),
    ]
