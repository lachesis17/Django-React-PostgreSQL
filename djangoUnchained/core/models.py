from django.db import models

class CptData(models.Model):
    depth = models.FloatField()
    qc = models.FloatField(null=True)
    fs = models.FloatField(null=True)
    u = models.FloatField(null=True)

    def __str__(self):
        return f"{self.depth} - QC: {self.qc}, FS: {self.fs}, U: {self.u}"
    
'''==================================== PROJECT ===================================='''

class PROJ(models.Model):
    PROJ_ID = models.CharField(primary_key=True, max_length=50, verbose_name='Project Identifier')
    PROJ_NAME = models.CharField(max_length=255, verbose_name='Name')
    PROJ_LOC = models.CharField(max_length=255, verbose_name='Location')
    PROJ_CLNT = models.CharField(max_length=255, blank=True, verbose_name='Client')
    PROJ_CONT = models.CharField(max_length=255, blank=True, verbose_name='Contractor')
    PROJ_ENG = models.CharField(max_length=255, blank=True, verbose_name='Project Engineer')
    PROJ_MEMO = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')

    def __str__(self):
        return f"{self.PROJ_ID} - {self.PROJ_NAME} Client: {self.PROJ_CLNT}"
    
'''==================================== LOCATION ===================================='''
    
class LOCA(models.Model):
    PROJ_ID = models.OneToOneField(PROJ, on_delete=models.CASCADE, related_name='locations',verbose_name='Project ID')

    LOCA_ID = models.CharField(primary_key=True, max_length=50, verbose_name='Location')
    LOCA_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Type of Activity')
    LOCA_STAT = models.CharField(max_length=50, blank=True, verbose_name='Status of Information Relating to this Position')
    LOCA_NATE = models.FloatField(null=True, verbose_name='National Grid Easting of Location or Start of Traverse')
    LOCA_NATN = models.FloatField(null=True, verbose_name='National Grid Northing of Location or Start of Traverse')
    LOCA_GREF = models.CharField(max_length=50, blank=True, verbose_name='National Grid Referencing System Used')
    LOCA_GL = models.FloatField(null=True, verbose_name='Ground Level Relative to Datum of Location or Start of Traverse')
    LOCA_REM = models.TextField(max_length=255, blank=True, verbose_name='General Remarks')
    LOCA_FDEP = models.FloatField(verbose_name='Final Depth')
    LOCA_STAR = models.DateTimeField(blank=True, verbose_name='Date of Start of Activity')
    LOCA_PURP = models.CharField(max_length=255, blank=True, verbose_name='Purpose of Activity at this Location')
    LOCA_TERM = models.CharField(max_length=255, blank=True, verbose_name='Reason for Activity Termination')
    LOCA_ENDD = models.DateTimeField(blank=True, verbose_name='End Date of Activity')
    LOCA_LETT = models.CharField(max_length=50, blank=True, verbose_name='OSGB Letter Grid Reference')
    LOCA_LOCX = models.FloatField(null=True, verbose_name='Local Grid X Coordinate or Start of Traverse')
    LOCA_LOCY = models.FloatField(null=True, verbose_name='Local Grid Y Coordinate or Start of Traverse')
    LOCA_LOCZ = models.FloatField(null=True, verbose_name='Level or Start of Traverse to Local Datum')
    LOCA_LREF = models.CharField(max_length=50, blank=True, verbose_name='Local Grid Referencing System Used')
    LOCA_DATM = models.CharField(max_length=50, blank=True, verbose_name='Local Datum Referencing System Used')
    LOCA_ETRV = models.FloatField(null=True, verbose_name='National Grid Easting of End of Traverse')
    LOCA_NTRV = models.FloatField(null=True, verbose_name='National Grid Northing of End of Traverse')
    LOCA_LTRV = models.FloatField(null=True, verbose_name='Ground Level Relative to Datum of End of Traverse')
    LOCA_XTRL = models.FloatField(null=True, verbose_name='Local Grid Easting of End of Traverse')
    LOCA_YTRL = models.FloatField(null=True, verbose_name='Local Grid Northing of End of Traverse')
    LOCA_ZTRL = models.FloatField(null=True, verbose_name='Local Elevation of End of Traverse')
    LOCA_LAT = models.CharField(max_length=50, blank=True, verbose_name='Latitude of Location or Start of Traverse')
    LOCA_LON = models.CharField(max_length=50, blank=True, verbose_name='Longitude of Location or Start of Traverse')
    LOCA_ELAT = models.CharField(max_length=50, blank=True, verbose_name='Latitude of End of Traverse')
    LOCA_ELON = models.CharField(max_length=50, blank=True, verbose_name='Longitude of End of Traverse')
    LOCA_LLIZ = models.CharField(max_length=50, blank=True, verbose_name='Projection Format')
    LOCA_LOCM = models.CharField(max_length=50, blank=True, verbose_name='Method of Location')
    LOCA_LOCA = models.CharField(max_length=50, blank=True, verbose_name='Site Location Sub Division (within Project)')
    LOCA_CLST = models.CharField(max_length=50, blank=True, verbose_name='Investigation Phase Grouping Code or Description')
    LOCA_ALID = models.CharField(max_length=50, blank=True, verbose_name='Alignment Identifier')
    LOCA_OFFS = models.FloatField(null=True, verbose_name='Offset')
    LOCA_CNGE = models.CharField(max_length=50, blank=True, verbose_name='Chainage')
    LOCA_TRAN = models.TextField(blank=True, verbose_name='Details of Algorithm Used to Calculate Local Grid Reference')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')
    LOCA_NATD = models.CharField(max_length=50, blank=True, verbose_name='National Datum Referencing System Used')
    LOCA_ORID = models.CharField(max_length=50, blank=True, verbose_name='Original Hole ID')
    LOCA_ORJO = models.CharField(max_length=50, blank=True, verbose_name='Original Job Reference')
    LOCA_ORCO = models.CharField(max_length=50, blank=True, verbose_name='Originating Company')

    def __str__(self):
        return f"{self.LOCA_ID}"
    
    def get_location_details(self):
        return f"{self.LOCA_ID} Type: {self.LOCA_TYPE} Hole Depth: {self.LOCA_FDEP} Water Depth: {self.LOCA_GL}"
    
    def get_location_easting_northing(self):
        return f"{self.LOCA_NATE}E {self.LOCA_NATN}N"
    
    def get_start_end(self):
        return f"Start: {self.LOCA_STAR} End: {self.LOCA_ENDD}"
    
'''==================================== SAMPLE INFORMATION ===================================='''
    
class SAMP(models.Model):
    LOCA_ID = models.OneToOneField(LOCA, on_delete=models.CASCADE, related_name='samples')

    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=50, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, verbose_name='Sample Type')
    SAMP_ID = models.CharField(primary_key=True, max_length=50, verbose_name='Sample Unique Identifier')
    SAMP_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Sample')
    SAMP_DTIM = models.DateTimeField(blank=True, verbose_name='Date and Time Sample Taken')
    SAMP_UBLO = models.FloatField(null=True, verbose_name='Number of Blows Required to Drive Sampler')
    SAMP_CONT = models.CharField(max_length=255, blank=True, verbose_name='Sample Container')
    SAMP_PREP = models.CharField(max_length=255, blank=True, verbose_name='Details of Sample Preparation at Time of Sampling')
    SAMP_SDIA = models.FloatField(null=True, verbose_name='Sample Diameter')
    SAMP_WDEP = models.FloatField(null=True, verbose_name='Depth to Water Below Ground Surface at Time of Sampling')
    SAMP_RECV = models.FloatField(null=True, verbose_name='Percentage of Sample Recovered')
    SAMP_TECH = models.CharField(max_length=50, blank=True, verbose_name='Sampling Technique/Method')
    SAMP_MATX = models.CharField(max_length=50, blank=True, verbose_name='Sample Matrix')
    SAMP_TYPC = models.CharField(max_length=50, blank=True, verbose_name='Sample QA Type (Normal, Blank or Spike)')
    SAMP_WHO = models.CharField(max_length=50, blank=True, verbose_name='Samplers Initials or Name')
    SAMP_WHY = models.CharField(max_length=255, blank=True, verbose_name='Reason for Sampling')
    SAMP_REM = models.TextField(blank=True, verbose_name='Sample Remarks')
    SAMP_DESC = models.CharField(max_length=255, blank=True, verbose_name='Sample/Specimen Description')
    SAMP_DESD = models.DateField(blank=True, verbose_name='Date Sample Described')
    SAMP_LOG = models.CharField(max_length=50, blank=True, verbose_name='Person Responsible for Sample/Specimen Description')
    SAMP_COND = models.CharField(max_length=255, blank=True, verbose_name='Condition and Representativeness of Sample')
    SAMP_CLSS = models.CharField(max_length=50, blank=True, verbose_name='Sample Classification as Required by EN ISO 14688-1')
    SAMP_BAR = models.FloatField(null=True, verbose_name='Barometric Pressure at Time of Sampling')
    SAMP_TEMP = models.FloatField(null=True, verbose_name='Sample Temperature at Time of Sampling')
    SAMP_PRES = models.FloatField(null=True, verbose_name='Gas Pressure (Above Barometric)')
    SAMP_FLOW = models.FloatField(null=True, verbose_name='Gas Flow Rate')
    SAMP_ETIM = models.DateTimeField(null=True, verbose_name='Date and Time Sampling Completed')
    SAMP_DURN = models.TimeField(blank=True, verbose_name='Sampling Duration')
    SAMP_CAPT = models.CharField(max_length=255, blank=True, verbose_name='Caption Used to Describe Sample')
    SAMP_LINK = models.CharField(max_length=255, blank=True, verbose_name='Sample Record Link')
    GEOL_STAT = models.CharField(max_length=50, blank=True, verbose_name='Stratum Reference Shown on Trial Pit or Traverse Sketch')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference (SSDS)')
    SAMP_RECL = models.FloatField(null=True, verbose_name='Length of Sample Recovered')

    def __str__(self):
        return f"{self.SAMP_ID} - {self.SAMP_TYPE}"
    
    def get_sample(self):
        return f"{self.LOCA_ID} - Top Depth: {self.SAMP_TOP} Ref: {self.SAMP_REF} Type: {self.SAMP_TYPE} ID: {self.SAMP_ID}"
    
'''==================================== CORING ===================================='''

class CORE(models.Model):
    LOCA_ID = models.ForeignKey(LOCA, on_delete=models.CASCADE, related_name='coring', verbose_name='Location')

    CORE_TOP = models.FloatField(verbose_name='Depth to Top of Core Run')
    CORE_BASE = models.FloatField(verbose_name='Depth to Base of Core Run')
    CORE_PREC = models.FloatField(verbose_name='Percentage of Core Recovered in Core Run')
    CORE_SREC = models.FloatField(verbose_name='Percentage of Solid Core Recovered in Core Run')
    CORE_RQD = models.FloatField(verbose_name='Rock Quality Designation for Core Run')
    CORE_DIAM = models.FloatField(verbose_name='Core Diameter')
    CORE_DURN = models.TimeField(verbose_name='Time Taken to Drill Core Run')
    CORE_REM = models.TextField(verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference')

    def __str__(self):
        return f"{self.LOCA_ID} - Top Depth: {self.CORE_TOP} Base Depth: {self.CORE_BASE} Core Rec: {self.CORE_PREC}% Solid Rec: {self.CORE_SREC}% RQD: {self.CORE_RQD}"
    
'''==================================== GEOLOGY ===================================='''

class GEOL(models.Model):
    LOCA_ID = models.ForeignKey(LOCA, on_delete=models.CASCADE, related_name='geology_descriptions', verbose_name='Location')

    GEOL_TOP = models.FloatField(primary_key=True, verbose_name='Depth to the Top of Stratum (m)')
    GEOL_BASE = models.FloatField(verbose_name='Depth to the Base of Description (m)')
    GEOL_DESC = models.TextField(verbose_name='General Description of Stratum', blank=True)
    GEOL_LEG = models.CharField(max_length=50, verbose_name='Legend Code (Soil Type)')
    GEOL_GEOL = models.CharField(max_length=50, verbose_name='Geology Code (Soil Unit)', blank=True)
    GEOL_GEO2 = models.CharField(max_length=50, verbose_name='Second Geology Code (Soil Unit)', blank=True)
    GEOL_STAT = models.CharField(max_length=50, verbose_name='Stratum Reference Shown on Trial Pit or Traverse Sketch', blank=True)
    GEOL_BGS = models.CharField(max_length=50, verbose_name='BGS Lexicon Code', blank=True)
    GEOL_FORM = models.CharField(max_length=255, verbose_name='Geological Formation or Stratum Name', blank=True)
    GEOL_REM = models.TextField(verbose_name='Remarks', blank=True)
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference', blank=True)

    def __str__(self):
        return f"{self.LOCA_ID} - {self.GEOL_DESC}"
    
    def get_layers(self):
        return f"Loca: {self.LOCA_ID} Top: {self.GEOL_TOP} Bot: {self.GEOL_BASE} Soil Type: {self.GEOL_LEG}"
    
class DREM(models.Model):
    LOCA_ID = models.ForeignKey(LOCA, on_delete=models.CASCADE, related_name='depth_remarks', verbose_name='Location')

    DREM_TOP = models.FloatField(primary_key=True, verbose_name='Depth to the Top of Stratum (m)')
    DREM_BASE = models.FloatField(verbose_name='Depth to the Base of Description (m)')
    DREM_REM = models.TextField(verbose_name='Remarks', blank=True)
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference', blank=True)

    def __str__(self):
        return f"{self.LOCA_ID} - {self.DREM_REM}"
    
    def get_layers(self):
        return f"Loca: {self.LOCA_ID} Top: {self.DREM_TOP} Bot: {self.DREM_BASE} Desc: {self.DREM_REM}"
    
'''==================================== CPT DATA ===================================='''

class SCPG(models.Model):
    LOCA_ID = models.ForeignKey(LOCA, on_delete=models.CASCADE, related_name='cpt_general', verbose_name='Location')

    SCPG_TESN = models.CharField(primary_key=True, max_length=50, verbose_name='Test Reference or Push Number')
    SCPG_DEPTH = models.FloatField(verbose_name='Top Depth of Cone Push')
    SCPG_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Cone Test Type')
    SCPG_REF = models.CharField(max_length=50, blank=True, verbose_name='Cone Reference')
    SCPG_CSA = models.FloatField(null=True, verbose_name='Surface Area of Cone Tip')
    SCPG_RATE = models.FloatField(null=True, verbose_name='Nominal Rate of Penetration of the Cone')
    SCPG_FILT = models.CharField(max_length=50, blank=True, verbose_name='Type of Filter Material Used')
    SCPG_FRIC = models.CharField(max_length=2, blank=True, verbose_name='Friction Reducer Used')
    SCPG_WAT = models.FloatField(null=True, verbose_name='Groundwater Level at Time of Test')
    SCPG_WATA = models.CharField(max_length=255, blank=True, verbose_name='Origin of Water Level in SCPG_WAT')
    SCPG_REM = models.TextField(blank=True, verbose_name='Comments on Testing and Basis of Any Interpreted Parameters Included in SCPT and SCPP')
    SCPG_ENV = models.CharField(max_length=255, blank=True, verbose_name='Details of Weather and Environmental Conditions During Test')
    SCPG_CONT = models.CharField(max_length=255, blank=True, verbose_name='Subcontractors Name')
    SCPG_METH = models.CharField(max_length=50, blank=True, verbose_name='Standard Followed for Testing')
    SCPG_CRED = models.CharField(max_length=255, blank=True, verbose_name='Accrediting Body and Reference Number')
    SCPG_CAR = models.FloatField(null=True, verbose_name='Cone Area Ratio Used to Calculate qt')
    SCPG_SLAR = models.FloatField(null=True, verbose_name='Sleeve Area Ratio Used to Calculate ft')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference (Cone Certificates)')

    def __str__(self):
        return f"{self.SCPG_TESN} - {self.SCPG_DEPTH}m"

class SCPT(models.Model):
    SCPG_TESN = models.OneToOneField(SCPG, on_delete=models.CASCADE, related_name='cpt_test', verbose_name='Cone ID')

    SCPT_DPTH = models.FloatField(primary_key=True, verbose_name='Depth of Res`ult` (m)')
    SCPT_RES = models.FloatField(verbose_name='Cone Resistance (qc) (MPa)')
    SCPT_FRES = models.FloatField(verbose_name='Local Unit Side Friction Resistance (fs) (MPa)')
    SCPT_PWP1 = models.FloatField(verbose_name='Face Porewater Pressure (u1) (kPa)')
    SCPT_PWP2 = models.FloatField(null=True, verbose_name='Shoulder Porewater Pressure (u2) (kPa)')
    SCPT_PWP3 = models.FloatField(null=True, verbose_name='Top of Sleeve Porewater Pressure (u3) (kPa)')
    SCPT_CON = models.FloatField(null=True, verbose_name='Conductivity (us/cm)')
    SCPT_TEMP = models.FloatField(null=True, verbose_name='Temperature (°C)')
    SCPT_PH = models.FloatField(null=True, verbose_name='pH Reading')
    SCPT_SLP1 = models.FloatField(null=True, verbose_name='Slope Indicator No. 1 (deg)')
    SCPT_SLP2 = models.FloatField(null=True, verbose_name='Slope Indicator No. 2 (deg)')
    SCPT_REDX = models.FloatField(null=True, verbose_name='Redox Potential Reading (mV)')
    SCPT_MAGT = models.FloatField(null=True, verbose_name='Magnetic Flux - Total (nT)')
    SCPT_MAGX = models.FloatField(null=True, verbose_name='Magnetic Flux - X (nT)')
    SCPT_MAGY = models.FloatField(null=True, verbose_name='Magnetic Flux - Y (nT)')
    SCPT_MAGZ = models.FloatField(null=True, verbose_name='Magnetic Flux - Z (nT)')
    SCPT_SMP = models.FloatField(null=True, verbose_name='Soil Moisture (%)')
    SCPT_NGAM = models.FloatField(null=True, verbose_name='Natural Gamma Radiation (counts/s)')
    SCPT_REM = models.TextField(verbose_name='Remarks')
    SCPT_FRR = models.FloatField(null=True, verbose_name='Friction Ratio (Rf) (%)')
    SCPT_QT = models.FloatField(null=True, verbose_name='Corrected Cone Resistance (qt) (MPa)')
    SCPT_FT = models.FloatField(null=True, verbose_name='Corrected Sleeve Resistance (ft) (MPa)')
    SCPT_QE = models.FloatField(null=True, verbose_name='Effective Cone Resistance (qe) (MPa)')
    SCPT_BDEN = models.FloatField(null=True, verbose_name='Bulk Density of Material (Mg/m3)')
    SCPT_CPO = models.FloatField(null=True, verbose_name='Total Vertical Stress (kPa)')
    SCPT_CPOD = models.FloatField(null=True, verbose_name='Effective Vertical Stress (kPa)')
    SCPT_QNET = models.FloatField(null=True, verbose_name='Net Cone Resistance (qn) (MPa)')
    SCPT_FRRC = models.FloatField(null=True, verbose_name='Corrected Friction Ratio (Rf) (%)')
    SCPT_EXPP = models.FloatField(null=True, verbose_name='Excess Pore Pressure (u-u0) (MPa)')
    SCPT_BQ = models.FloatField(null=True, verbose_name='Pore Pressure Ratio (Bq)')
    SCPT_ISPP = models.FloatField(null=True, verbose_name='In Situ Pore Pressure (u0) (MPa)')
    SCPT_NQT = models.FloatField(null=True, verbose_name='Normalised Cone Resistance (Qt)')
    SCPT_NFR = models.FloatField(null=True, verbose_name='Normalised Friction Ratio (Fr) (%)')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference (Raw Field Data)')

    def __str__(self):
        return f"{self.SCPG_TESN} - Depth: {self.SCPT_DPTH}m"
    
'''==================================== SESIMIC ===================================='''

class SCCG(models.Model):
    LOCA_ID = models.ForeignKey(LOCA, on_delete=models.CASCADE, related_name='seismic_general', verbose_name='Location')

    SCCG_TESN = models.CharField(primary_key=True, max_length=50, verbose_name='Cone ID')
    SCCG_TYPE = models.CharField(max_length=50, verbose_name='Seismic CPT test type')
    SCCG_REF = models.CharField(max_length=50, verbose_name='Cone reference')
    SCCG_HAM = models.CharField(max_length=50, verbose_name='Shear hammer setup')
    SCCG_SHOF = models.FloatField(verbose_name='Horizontal offset between centre of cone and source')
    SCCG_SELE = models.FloatField(verbose_name='Source elevation above seabed')
    SCCG_ZLOC = models.CharField(max_length=50, verbose_name='Location where the zero reading of the cone has been performed for a given push')
    SCCG_OTOP = models.FloatField(verbose_name='Offset between centre of the top receiver and the cone tip')
    SCCG_OBOT = models.FloatField(verbose_name='Offset between centre of the bottom receiver and the cone tip')
    SCCG_REM = models.TextField(verbose_name='Remarks')

class SCCT(models.Model):
    SCCG_TESN = models.OneToOneField(SCCG, on_delete=models.CASCADE, related_name='seismic_test', verbose_name='Cone ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location')
    SCCT_GEOP = models.CharField(max_length=50, verbose_name='Selected receiver component')
    SCCT_HDIR = models.CharField(max_length=50, verbose_name='Selected hammer direction')
    SCCT_METH = models.CharField(max_length=50, verbose_name='Selected method for interval velocity')
    SCCT_SWVL = models.FloatField(verbose_name='Final shear wave velocity (Vs final)')
    SCCT_SWD = models.FloatField(verbose_name='Depth corresponding to shear wave velocity measurement')
    SCCT_SWC = models.FloatField(verbose_name='Confidence interval of shear wave velocity')
    SCCT_REM = models.TextField(verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File reference')

'''==================================== PS LOGGING ===================================='''

class PSLG(models.Model):
    LOCA_ID = models.ForeignKey(LOCA, on_delete=models.CASCADE, related_name='ps_logging_general', verbose_name='Location')

    PSLG_TESN = models.CharField(primary_key=True, max_length=50, blank=True, verbose_name='Test number')
    PSLG_DIAM = models.FloatField(null=True, verbose_name='Expected hole diameter/bit size')
    PSLG_CADE = models.FloatField(null=True, verbose_name='Casing shoe depth below seabed')
    PSLG_REM = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')

class PSLT(models.Model):
    PSLG_TESN = models.OneToOneField(PSLG, on_delete=models.CASCADE, related_name='ps_logging_test', verbose_name='Location')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location')
    PSLT_DPTH = models.FloatField(verbose_name='Logging depth below seabed')
    PSLT_P = models.FloatField(verbose_name='P-wave velocity')
    PSLT_S = models.FloatField(verbose_name='S-wave velocity')
    PSLT_BDEN = models.FloatField(verbose_name='Bulk density from gamma-gamma tool')
    PSLT_CLPR = models.FloatField(verbose_name='Caliper measurement of equivalent hole diameter')
    PSLT_NGAM = models.FloatField(verbose_name='Natural gamma')
    PSLT_PVTC = models.CharField(max_length=50, verbose_name='P-wave trace class')
    PSLT_SVTC = models.CharField(max_length=50, verbose_name='S-wave trace class')
    PSLT_REM = models.TextField(verbose_name='Remarks')


'''==================================== LAB RESULTS ===================================='''

'''=================================== CLASSIFICATION ===================================='''

'''==================================== MOISTURE ===================================='''

class LNMC(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='moisture_content', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample (m)')
    SAMP_REF = models.CharField(max_length=50, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, verbose_name='Specimen Reference')
    SPEC_DEPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen (m)')
    SPEC_DESC = models.TextField(verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(verbose_name='Details of Specimen Preparation')
    LNMC_MC = models.FloatField(verbose_name='Water/Moisture Content (%)')
    LNMC_TEMP = models.FloatField(verbose_name='Temperature Sample Dried at (°C)')
    LNMC_STAB = models.FloatField(verbose_name='Amount of Stabiliser Added (%)')
    LNMC_STYP = models.CharField(max_length=50, verbose_name='Type of Stabiliser Added')
    LNMC_INST = models.CharField(max_length=2, verbose_name='Is Test Result Assumed to be Natural Water/Moisture Content')
    LNMC_COMM = models.TextField(verbose_name='Reason Water/Moisture Content is Assumed to be Other than Natural')
    LNMC_REM = models.TextField(verbose_name='Remarks')
    LNMC_METH = models.CharField(max_length=50, verbose_name='Test Method')
    LNMC_LAB = models.CharField(max_length=100, verbose_name='Name of Testing Laboratory/Organization')
    LNMC_CRED = models.CharField(max_length=50, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=50, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference')
    SPEC_BASE = models.FloatField(verbose_name='Depth to Base of Specimen (m)')
    LNMC_DEV = models.TextField(verbose_name='Deviation from the Specified Procedure', blank=True, null=True)

    def __str__(self):
        return f"{self.SAMP_ID} - Moisture Content: {self.LNMC_MC}%"
    
'''==================================== DENSITY ===================================='''
    
class LDEN(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='bulk_density', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample (m)')
    SAMP_REF = models.CharField(max_length=50, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen (m)')
    SPEC_DESC = models.TextField(verbose_name='Specimen Description', blank=True)
    SPEC_PREP = models.TextField(verbose_name='Specimen Preparation Details', blank=True)
    LDEN_TYPE = models.CharField(max_length=50, verbose_name='Type of Test Performed', blank=True)
    LDEN_COND = models.CharField(max_length=50, verbose_name='Sample Condition', blank=True)
    LDEN_SMITY = models.CharField(max_length=50, verbose_name='Type of Sample', blank=True)
    LDEN_MC = models.FloatField(verbose_name='Water/Moisture Content (%)', null=True)
    LDEN_BDEN = models.FloatField(verbose_name='Bulk Density (Mg/m³)', null=True)
    LDEN_DDEN = models.FloatField(verbose_name='Dry Density (Mg/m³)', null=True)
    LDEN_REM = models.TextField(verbose_name='Remarks', blank=True)
    LDEN_METH = models.CharField(max_length=100, verbose_name='Test Method', blank=True)
    LDEN_LAB = models.CharField(max_length=100, verbose_name='Laboratory Name', blank=True)
    LDEN_CRED = models.CharField(max_length=50, verbose_name='Accrediting Body and Reference', blank=True)
    TEST_STAT = models.CharField(max_length=50, verbose_name='Test Status', blank=True)
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference', blank=True)
    SPEC_BASE = models.FloatField(verbose_name='Depth to Base of Specimen (m)', null=True)
    LDEN_DEV = models.CharField(max_length=255, verbose_name='Deviation from Standard Procedure', blank=True)

    def __str__(self):
        return f"{self.SAMP_ID} - BDEN: {self.LDEN_BDEN} DDEN: {self.LDEN_DDEN}"
    
'''==================================== PSD ===================================='''

class GRAG(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='particle_size_distribution', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample (m)')
    SAMP_REF = models.CharField(max_length=50, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, verbose_name='Specimen Reference')
    SPEC_DEPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen (m)')
    SPEC_DESC = models.TextField(verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(verbose_name='Details of Specimen Preparation')
    GRAG_UC = models.FloatField(verbose_name='Uniformity Coefficient (D60/D10)')
    GRAG_CC = models.FloatField(verbose_name='Coefficient of Curvature')
    GRAG_VCRE = models.FloatField(verbose_name='Percentage of Material Tested Greater than 63mm (%)')
    GRAG_GRAV = models.FloatField(verbose_name='Percentage of Material Tested in Range 63mm to 2mm (%)')
    GRAG_SAND = models.FloatField(verbose_name='Percentage of Material Tested in Range 2mm to 63um (%)')
    GRAG_SILT = models.FloatField(verbose_name='Percentage of Material Tested in Range 63um to 2um (%)')
    GRAG_CLAY = models.FloatField(verbose_name='Percentage of Material Tested Less than 2um (%)')
    GRAG_FINE = models.FloatField(verbose_name='Percentage Less than 63um (%)')
    GRAG_REM = models.TextField(verbose_name='Remarks')
    GRAG_METH = models.CharField(max_length=100, verbose_name='Test Method')
    GRAG_LAB = models.CharField(max_length=100, verbose_name='Name of Testing Laboratory/Organization')
    GRAG_CRED = models.CharField(max_length=50, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=50, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File reference')
    SPEC_BASE = models.FloatField(verbose_name='Depth to Base of Specimen (m)')
    GRAG_DEV = models.TextField(verbose_name='Deviation from the Specified Test Procedure')
    GRAG_PDEN = models.FloatField(verbose_name='Particle Density (Mg/m3)')
    GRAG_PRET = models.CharField(max_length=255, verbose_name='Method of Pre-treatment')
    GRAG_SUFF = models.CharField(max_length=2, verbose_name='Sufficiency of Soil Tested')
    GRAG_EXCL = models.TextField(verbose_name='Exclusion Remark')
    GRAG_D10 = models.FloatField(null=True, verbose_name='Sieve size at which 10%\ of the material passes through')      # NON-STANDARD
    GRAG_D50 = models.FloatField(null=True, verbose_name='Sieve size at which 50%\ of the material passes through')      # NON-STANDARD
    GRAG_D60 = models.FloatField(null=True, verbose_name='Sieve size at which 60%\ of the material passes through')      # NON-STANDARD

    def __str__(self):
        return f"{self.SAMP_ID} - {self.GRAG_FINE}% fines"
    
class GRAT(models.Model):
    SAMP_ID = models.ForeignKey(GRAG, on_delete=models.CASCADE, related_name='particle_size_distribution_data', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample (m)')
    SAMP_REF = models.CharField(max_length=50, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen (m)', help_text="m")
    GRAT_SIZE = models.FloatField(verbose_name='Sieve or Particle Size (mm)', help_text="mm")
    GRAT_PERP = models.FloatField(verbose_name='Percentage Passing/Finer than GRAT_SIZE (%)', help_text="%")
    GRAT_TYPE = models.CharField(max_length=50, verbose_name='Test Type')
    GRAT_REM = models.TextField(verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File reference')
    
    def __str__(self):
        return f"{self.SAMP_ID} - {self.GRAT_SIZE} mm - {self.GRAT_PERP} passing (%)"

'''==================================== ATTERBERG ===================================='''

class LLPL(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='atterberg', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=50, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of Specimen Preparation')
    LLPL_LL = models.FloatField(null=True, verbose_name='Liquid Limit')
    LLPL_PL = models.FloatField(null=True, verbose_name='Plastic Limit')
    LLPL_PI = models.FloatField(null=True, verbose_name='Plasticity Index')
    LLPL_425 = models.FloatField(null=True, verbose_name='Percentage Passing 0.425mm Sieve')
    LLPL_PREP = models.CharField(max_length=50, blank=True, verbose_name='Method of Preparation')
    LLPL_STAB = models.FloatField(null=True, verbose_name='Amount of Stabiliser Added')
    LLPL_STYP = models.CharField(max_length=50, blank=True, verbose_name='Type of Stabiliser Added')
    LLPL_REM = models.TextField(blank=True, verbose_name='Remarks')
    LLPL_METH = models.CharField(max_length=50, blank=True, verbose_name='Test Method')
    LLPL_LAB = models.CharField(max_length=255, blank=True, verbose_name='Name of Testing Laboratory/Organization')
    LLPL_CRED = models.CharField(max_length=50, blank=True, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=50, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    LLPL_DEV = models.CharField(max_length=50, blank=True, verbose_name='Deviation from the Specified Procedure')
    LLPL_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Type of Test')
    LLPL_POIN = models.CharField(max_length=50, blank=True, verbose_name='Number of Points')
    LLPL_CONE = models.CharField(max_length=50, blank=True, verbose_name='For Cone Method, Type of Cone')
    LLPL_1PRE = models.FloatField(null=True, verbose_name='Mean of Test Readings, if One-Point Test')
    LLPL_1PCF = models.FloatField(null=True, verbose_name='Correlation Factor if One-Point Test')
    LLPL_SIZE = models.FloatField(null=True, verbose_name='Sieve Size if Other than 0.425mm')
    LLPL_PASS = models.FloatField(null=True, verbose_name='Percentage Passing LLPL_SIZE Sieve if Other than 0.425mm')
    LLPL_WC = models.FloatField(null=True, verbose_name='Water Content of the Specimen Before Removal of Particles')

    def __str__(self):
        return f"{self.SAMP_ID} - LL: {self.LLPL_LL} PL: {self.LLPL_PL} PI: {self.LLPL_PI}"

'''==================================== PARTICLE DENSITY ===================================='''

class LPDN(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='particle_density', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=50, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of Specimen Preparation')
    LPDN_PDEN = models.FloatField(null=True, verbose_name='Particle Density (Mg/m³)')
    LPDN_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Type of Test')
    LPDN_REM = models.TextField(blank=True, verbose_name='Remarks')
    LPDN_METH = models.CharField(max_length=50, blank=True, verbose_name='Test Method')
    LPDN_LAB = models.CharField(max_length=255, blank=True, verbose_name='Name of Testing Laboratory/Organization')
    LPDN_CRED = models.CharField(max_length=50, blank=True, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=50, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    LPDN_DEV = models.TextField(blank=True, verbose_name='Deviation from the Specified Test Procedure')
    LPDN_PVOL = models.FloatField(null=True, verbose_name='Pycnometer Volume if Used and Not 50ml')
    LPDN_GAS = models.CharField(max_length=50, blank=True, verbose_name='Identity of Gas if Pycnometer Used')

    def __str__(self):
        return f"{self.SAMP_ID} - SG: {self.LPDN_PDEN}"
    
'''==================================== ELECTRICAL ===================================='''
    
class LRES(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='electrical_resistivity', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=50, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of Specimen Preparation')
    LRES_BDEN = models.FloatField(null=True, verbose_name='Bulk Density (Mg/m³)')
    LRES_DDEN = models.FloatField(null=True, verbose_name='Dry Density (Mg/m³)')
    LRES_MC = models.FloatField(null=True, verbose_name='Water/Moisture Content (%)')
    LRES_COND = models.TextField(blank=True, verbose_name='Sample Condition Details')
    LRES_LRES = models.FloatField(null=True, verbose_name='Temperature Corrected Resistivity (ohm m)')
    LRES_CDIA = models.FloatField(null=True, verbose_name='Diameter of Container (mm)')
    LRES_CCSA = models.FloatField(null=True, verbose_name='Container Cross-Sectional Area (mm²)')
    LRES_CLEN = models.FloatField(null=True, verbose_name='Length of Container (mm)')
    LRES_TEMP = models.FloatField(null=True, verbose_name='Temperature at Which Test Performed (°C)')
    LRES_ELEC = models.TextField(blank=True, verbose_name='Type of Electrodes')
    LRES_PENT = models.TextField(blank=True, verbose_name='Probes Dimensions and Details')
    LRES_CSHP = models.CharField(max_length=50, blank=True, verbose_name='Shape of Container')
    LRES_WAT = models.FloatField(null=True, verbose_name='Volume of Water (ml)')
    LRES_WRES = models.FloatField(null=True, verbose_name='Water Resistivity (ohm m)')
    LRES_PART = models.TextField(blank=True, verbose_name='Percentage of Large Particles Removed')
    LRES_REM = models.TextField(blank=True, verbose_name='Remarks')
    LRES_METH = models.CharField(max_length=255, blank=True, verbose_name='Test Method')
    LRES_LAB = models.CharField(max_length=255, blank=True, verbose_name='Testing Laboratory Name')
    LRES_CRED = models.CharField(max_length=50, blank=True, verbose_name='Accrediting Body Reference')
    TEST_STAT = models.CharField(max_length=50, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    LRES_DEV = models.TextField(blank=True, verbose_name='Deviation from Test Procedure')

    def __str__(self):
        return f"{self.SAMP_ID} - {self.LRES_LRES} (ohm m)"
    
'''==================================== THERMAL ===================================='''

class LTCH(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='thermal_conductivity', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=50, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of Specimen Preparation')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    LTCH_COND = models.TextField(blank=True, verbose_name='Sample Condition')
    LTCH_BDEN = models.FloatField(null=True, verbose_name='Bulk Density (Mg/m³)')
    LTCH_DDEN = models.FloatField(null=True, verbose_name='Dry Density (Mg/m³)')
    LTCH_MC = models.FloatField(null=True, verbose_name='Water/Moisture Content (%)')
    LTCH_TCON = models.FloatField(null=True, verbose_name='Thermal Conductivity (W/(K-m))')
    LTCH_TRES = models.FloatField(null=True, verbose_name='Thermal Resistivity (K-m/W)')
    LTCH_TEMP = models.FloatField(null=True, verbose_name='Ambient Temperature at Test (°C)')
    LTCH_PDIA = models.FloatField(null=True, verbose_name='Probe Diameter (mm)')
    LTCH_PSPA = models.FloatField(null=True, verbose_name='Probe Spacing (mm)')
    LTCH_PPEN = models.FloatField(null=True, verbose_name='Probe Penetration (mm)')
    LTCH_PRBE = models.TextField(blank=True, verbose_name='Method of Probe Insertion')
    LTCH_PART = models.TextField(blank=True, verbose_name='Particle Grain Size Removed')
    LTCH_DEV = models.TextField(blank=True, verbose_name='Deviation from the Procedure')
    LTCH_REM = models.TextField(blank=True, verbose_name='Remarks')
    LTCH_METH = models.CharField(max_length=255, blank=True, verbose_name='Test Method')
    LTCH_LAB = models.CharField(max_length=255, blank=True, verbose_name='Testing Laboratory Name')
    LTCH_CRED = models.CharField(max_length=50, blank=True, verbose_name='Accrediting Body Reference')
    TEST_STAT = models.CharField(max_length=50, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')

    def __str__(self):
        return f"{self.SAMP_ID} - Conductivity: {self.LTCH_TCON} (W/(K-m)) Resistivity: {self.LTCH_TRES} (K-m/W)"
    
'''==================================== MIN/MAX ===================================='''

class RELD(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='minmax', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=50, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of Specimen Preparation')
    RELD_DMAX = models.FloatField(null=True, verbose_name='Maximum Dry Density (Mg/m³)')
    RELD_375 = models.FloatField(null=True, verbose_name='Percent Retained on 37.5mm Sieve (%)')
    RELD_063 = models.FloatField(null=True, verbose_name='Percent Retained on 6.3mm Sieve (%)')
    RELD_020 = models.FloatField(null=True, verbose_name='Percent Retained on 2mm Sieve (%)')
    RELD_DMIN = models.FloatField(null=True, verbose_name='Minimum Dry Density (Mg/m³)')
    RELD_REM = models.TextField(blank=True, verbose_name='Remarks')
    RELD_METH = models.CharField(max_length=255, blank=True, verbose_name='Test Method')
    RELD_LAB = models.CharField(max_length=255, blank=True, verbose_name='Testing Laboratory Name')
    RELD_CRED = models.CharField(max_length=50, blank=True, verbose_name='Accrediting Body Reference')
    TEST_STAT = models.CharField(max_length=50, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    RELD_DEV = models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')

    def __str__(self):
        return f"{self.SAMP_ID} - Min: {self.RELD_DMIN} Max: {self.RELD_DMAX}"
    
from django.db import models

'''==================================== PERMEABILITY ===================================='''

class PTST(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='permeability', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=50, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    PTST_TESN = models.CharField(max_length=50, blank=True, verbose_name='Test Reference')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of Specimen Preparation')
    PTST_COND = models.CharField(max_length=50, blank=True, verbose_name='Sample Condition')
    PTST_SZUN = models.FloatField(null=True, verbose_name='Size Cut-off of Material Too Coarse for Testing')
    PTST_UNS = models.FloatField(null=True, verbose_name='Proportion of Material Removed Above PTST')
    PTST_DIAM = models.FloatField(null=True, verbose_name='Specimen Diameter')
    PTST_LEN = models.FloatField(null=True, verbose_name='Specimen Length')
    PTST_MC = models.FloatField(null=True, verbose_name='Initial Water/Moisture Content of Test Specimen')
    PTST_BDEN = models.FloatField(null=True, verbose_name='Initial Bulk Density of Test Specimen')
    PTST_DDEN = models.FloatField(null=True, verbose_name='Initial Dry Density')
    PTST_IDIA = models.FloatField(null=True, verbose_name='Diameter of Drain for Radial Permeability in Hydraulic Cell')
    PTST_DMET = models.TextField(blank=True, verbose_name='Method of Forming Central Drain')
    PTST_VOID = models.FloatField(null=True, verbose_name='Initial Voids Ratio')
    PTST_K = models.FloatField(null=True, verbose_name='Coefficient of Permeability')
    PTST_TSTR = models.FloatField(null=True, verbose_name='Mean Effective Stress at which Permeability Measured')
    PTST_HYGR = models.FloatField(null=True, verbose_name='Hydraulic Gradient at which Permeability Measured')
    PTST_ISAT = models.FloatField(null=True, verbose_name='Initial Degree of Saturation')
    PTST_SAT = models.TextField(blank=True, verbose_name='Details of Saturation')
    PTST_CONS = models.TextField(blank=True, verbose_name='Details of Consolidation')
    PTST_PDEN = models.FloatField(null=True, verbose_name='Particle Density with Prefix if Value Assumed')
    PTST_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Type of Permeability Measurement')
    PTST_CELL = models.CharField(max_length=50, blank=True, verbose_name='Type of Permeameter')
    PTST_REM = models.TextField(blank=True, verbose_name='Remarks')
    PTST_METH = models.CharField(max_length=50, blank=True, verbose_name='Test Method')
    PTST_LAB = models.CharField(max_length=255, blank=True, verbose_name='Name of Testing Laboratory/Organization')
    PTST_CRED = models.CharField(max_length=50, blank=True, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=50, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    PTST_DEV = models.TextField(blank=True, verbose_name='Deviations from the Test Method')
    PTST_WCIS = models.TextField(blank=True, verbose_name='Initial Water Content Source')
    PTST_WCF = models.FloatField(null=True, verbose_name='Final Water Content of Test Specimen')
    PTST_FSAT = models.FloatField(null=True, verbose_name='Final Degree of Saturation if Determined')
    PTST_TEMP = models.FloatField(null=True, verbose_name='Average Laboratory Temperature at which the Test was Performed')
    PTST_SOUR = models.TextField(blank=True, verbose_name='Source of Permeameter Water')
    PTST_BACK = models.FloatField(null=True, verbose_name='Back Pressure')
    PTST_BVAL = models.FloatField(null=True, verbose_name='B-Value, if Used')
    PTST_LOSS = models.TextField(blank=True, verbose_name='Equipment Head Loss Corrections Applied to the Measurements')

    def __str__(self):
        return f"{self.SAMP_ID} - K: {self.PTST_K} m/s"
    
'''==================================== CHEMICAL ===================================='''

class GCHM(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='chemical', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=50, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen')
    GCHM_CODE = models.CharField(max_length=50, verbose_name='Determinand')
    GCHM_METH = models.CharField(max_length=255, verbose_name='Test Method')
    GCHM_TYP = models.CharField(max_length=50, verbose_name='Test Type')
    GCHM_RESL = models.FloatField(verbose_name='Test Result')
    GCHM_UNIT = models.CharField(max_length=50, verbose_name='Test Result Units')
    GCHM_NAME = models.CharField(max_length=255, verbose_name='Client/Laboratory Preferred Name of Determinand')
    SPEC_DESC = models.TextField(verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(verbose_name='Details of Specimen Preparation')
    GCHM_REM = models.TextField(verbose_name='Remarks on Test')
    GCHM_LAB = models.CharField(max_length=255, verbose_name='Name of Testing Laboratory/Organization')
    GCHM_CRED = models.CharField(max_length=50, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=50, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference')
    GCHM_RTXT = models.TextField(verbose_name='Reported Result')
    GCHM_DLM = models.FloatField(verbose_name='Lower Detection Limit')
    SPEC_BASE = models.FloatField(verbose_name='Depth to Base of Specimen')
    GCHM_DEV = models.TextField(verbose_name='Deviations from the Test Method')
    GCHM_SGRP = models.CharField(max_length=50, verbose_name='Sample Delivery or Batch Code')
    GCHM_LSID = models.CharField(max_length=50, verbose_name='Laboratory Sample ID')
    GCHM_RDEV = models.TextField(verbose_name='Result Deviation Description')
    GCHM_RDAT = models.DateTimeField(verbose_name='Sample Receipt Date/Time at Laboratory')
    GCHM_DTIM = models.DateTimeField(verbose_name='Analysis Date and Time')
    GCHM_TEST = models.CharField(max_length=255, verbose_name='Test or Suite Name')
    GCHM_IREF = models.CharField(max_length=50, verbose_name='Instrument Reference or Identifier')
    GCHM_ITYP = models.CharField(max_length=50, verbose_name='Instrument Type')
    GCHM_SIZE = models.FloatField(verbose_name='Size of Material Removed Prior to Test')
    GCHM_PERP = models.FloatField(verbose_name='Percentage of Material Removed')

    def __str__(self):
        return f"{self.SAMP_ID} - Test: {self.GCHM_NAME} Code: {self.GCHM_CODE} Result: {self.GCHM_RESL} {self.GCHM_UNIT}"
    
from django.db import models

class ERES(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='chemical_environmental', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=50, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Sample type')
    SPEC_REF = models.CharField(max_length=50, blank=True, verbose_name='Laboratory specimen reference or Laboratory ID')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to top of test specimen')
    ERES_CODE = models.CharField(max_length=50, blank=True, verbose_name='Chemical code')
    ERES_METH = models.CharField(max_length=50, blank=True, verbose_name='Test method')
    ERES_MATX = models.CharField(max_length=50, blank=True, verbose_name='Laboratory test matrix')
    ERES_RTY = models.CharField(max_length=50, blank=True, verbose_name='Run type (Initial or Reanalysis)')
    ERES_TESN = models.CharField(max_length=50, blank=True, verbose_name='Test reference')
    ERES_NAME = models.CharField(max_length=50, blank=True, verbose_name='Chemical name')
    ERES_TNAM = models.CharField(max_length=50, blank=True, verbose_name='Laboratory analytical test name')
    ERES_RVAL = models.FloatField(null=True, verbose_name='Result value')
    ERES_RUNI = models.CharField(max_length=50, blank=True, verbose_name='Result unit')
    ERES_RTXT = models.CharField(max_length=50, blank=True, verbose_name='Reported result')
    ERES_RTC = models.CharField(max_length=50, blank=True, verbose_name='Result type')
    ERES_RRES = models.BooleanField(default=False, verbose_name='Reportable result')
    ERES_DETF = models.BooleanField(default=False, verbose_name='Detect flag')
    ERES_ORG = models.BooleanField(default=False, verbose_name='Organic')
    ERES_IQLF = models.CharField(max_length=50, blank=True, verbose_name='Interpreted qualifiers')
    ERES_LQLF = models.CharField(max_length=50, blank=True, verbose_name='Laboratory qualifiers')
    ERES_RDLM = models.FloatField(null=True, verbose_name='Reporting detection limit')
    ERES_MDL = models.FloatField(null=True, verbose_name='Method detection limit')
    ERES_QLM = models.FloatField(null=True, verbose_name='Quantification limit')
    ERES_DUIN = models.CharField(max_length=50, blank=True, verbose_name='Unit of detection / quantification limits')
    ERES_TIC = models.FloatField(null=True, verbose_name='Tentatively Identified Compound (TIC) probability')
    ERES_TICT = models.FloatField(null=True, verbose_name='Tentatively Identified Compound (TIC) retention time')
    ERES_RDAT = models.DateTimeField(null=True, verbose_name='Sample receipt date at laboratory')
    ERES_SGRP = models.CharField(max_length=50, blank=True, verbose_name='Sample delivery or batch code')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of specimen preparation including time between preparation and testing')
    SPEC_DESC = models.CharField(max_length=255, blank=True, verbose_name='Specimen description')
    ERES_DTIM = models.DateTimeField(null=True, verbose_name='Analysis date and time')
    ERES_TEST = models.CharField(max_length=50, blank=True, verbose_name='Test Name')
    ERES_TORD = models.CharField(max_length=50, blank=True, verbose_name='Total or dissolved')
    ERES_LOCN = models.CharField(max_length=50, blank=True, verbose_name='Analysis location')
    ERES_BAS = models.CharField(max_length=50, blank=True, verbose_name='Basis')
    ERES_DIL = models.FloatField(null=True, verbose_name='Dilution factor')
    ERES_LMTH = models.CharField(max_length=50, blank=True, verbose_name='Leachate method')
    ERES_LDTM = models.DateTimeField(null=True, verbose_name='Leachate preparation date and time')
    ERES_IRE = models.CharField(max_length=50, blank=True, verbose_name='Instrument Reference No or identifier')
    ERES_ITP = models.CharField(max_length=50, blank=True, verbose_name='Instrument type')
    ERES_SIZE = models.FloatField(null=True, verbose_name='Size of material removed prior to test')
    ERES_PER = models.FloatField(null=True, verbose_name='Percentage of material removed')
    ERES_REM = models.TextField(blank=True, verbose_name='Remarks')
    ERES_LAB = models.CharField(max_length=50, blank=True, verbose_name='Name of testing laboratory/Organization')
    ERES_CRED = models.CharField(max_length=50, blank=True, verbose_name='Accrediting body and reference number')
    TEST_STAT = models.CharField(max_length=50, blank=True, verbose_name='Test status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')

    def __str__(self):
        return f"{self.SAMP_ID} - Test: {self.ERES_NAME} Code: {self.ERES_CODE} Result: {self.ERES_RVAL} {self.ERES_RUNI}"
    
'''==================================== CONSOLIDATION ===================================='''

class CONG(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='consolidation_general', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=50, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Sample type')
    SPEC_REF = models.CharField(max_length=50, blank=True, verbose_name='Specimen reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to top of specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of specimen preparation including time between preparation and testing')
    CONG_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Type of consolidation test')
    CONG_COND = models.CharField(max_length=50, blank=True, verbose_name='Sample condition')
    CONG_SDIA = models.FloatField(null=True, verbose_name='Test specimen diameter')
    CONG_HIGT = models.FloatField(null=True, verbose_name='Test specimen height')
    CONG_MCI = models.FloatField(null=True, verbose_name='Initial water/moisture content')
    CONG_MCF = models.FloatField(null=True, verbose_name='Final water/moisture content')
    CONG_BDEN = models.FloatField(null=True, verbose_name='Initial bulk density')
    CONG_DDEN = models.FloatField(null=True, verbose_name='Initial dry density')
    CONG_PDEN = models.FloatField(null=True, verbose_name='Particle density')
    CONG_SATR = models.FloatField(null=True, verbose_name='Initial degree of saturation')
    CONG_SPRS = models.FloatField(null=True, verbose_name='Swelling pressure')
    CONG_SATH = models.FloatField(null=True, verbose_name='Height change of specimen on saturation or flooding')
    CONG_IVR = models.FloatField(null=True, verbose_name='Initial voids ratio')
    CONG_REM = models.TextField(blank=True, verbose_name='Remarks')
    CONG_METH = models.CharField(max_length=50, blank=True, verbose_name='Test method')
    CONG_LAB = models.CharField(max_length=50, blank=True, verbose_name='Name of testing laboratory/organization')
    CONG_CRED = models.CharField(max_length=50, blank=True, verbose_name='Accrediting body and reference number')
    TEST_STAT = models.CharField(max_length=50, blank=True, verbose_name='Test status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to base of specimen')
    CONG_DEV = models.TextField(blank=True, verbose_name='Deviations from the test method')
    CONG_MCIS = models.CharField(max_length=50, blank=True, verbose_name='Initial water/moisture content source')
    CONG_CORR = models.BooleanField(default=False, verbose_name='Results corrected for equipment deformation')
    CONG_EVES = models.FloatField(null=True, verbose_name='Effective Overburden')           # NON-STANDARD
    CONG_OCR = models.FloatField(null=True, verbose_name='Overconsolidation Ratio')         # NON-STANDARD
    CONG_RPCP = models.FloatField(null=True, verbose_name='Pre-consolidation Pressure ')    # NON-STANDARD
    CONG_RCOR = models.FloatField(null=True, verbose_name='Compression Index')              # NON-STANDARD
    CONG_IID = models.FloatField(null=True, verbose_name='Re-compression Index')            # NON-STANDARD
    CONG_SQ = models.FloatField(null=True, verbose_name='Sample Quality')                 # NON-STANDARD
    CONG_RSWP = models.FloatField(null=True, verbose_name='Swelling Pressure')              # NON-STANDARD
    CONG_SWLL = models.FloatField(null=True, verbose_name='Swell Index')                    # NON-STANDARD

    def __str__(self):
        return f"{self.SAMP_ID} - Type: {self.CONG_TYPE} Cond: {self.CONG_COND} Lab: {self.CONG_LAB} OCR: {self.CONG_OCR} Quality: {self.CONG_CSQ}"
    
class CONS(models.Model):
    SAMP_ID = models.ForeignKey(CONG, on_delete=models.CASCADE, related_name='consolidation_test', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=50, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Sample type')
    SPEC_REF = models.CharField(max_length=50, blank=True, verbose_name='Specimen reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to top of specimen')
    CONS_INCN = models.FloatField(blank=True, verbose_name='Oedometer stress increment')
    CONS_IVR = models.FloatField(null=True, verbose_name='Voids ratio at start of increment')
    CONS_INCF = models.FloatField(null=True, verbose_name='Stress at end of stress increment/decrement')
    CONS_INCE = models.FloatField(null=True, verbose_name='Voids ratio at end of stress increment')
    CONS_INMV = models.FloatField(null=True, verbose_name='Reported coefficient of volume compressibility over stress increment')
    CONS_INSC = models.FloatField(null=True, verbose_name='Coefficient of secondary compression over stress increment')
    CONS_CVRT = models.FloatField(null=True, verbose_name='Coefficient of consolidation over stress increment determined by the root time method')
    CONS_CVLG = models.FloatField(null=True, verbose_name='Coefficient of consolidation over stress increment determined by the log time method')
    CONS_TEMP = models.FloatField(null=True, verbose_name='Average temperature over stress increment')
    CONS_REM = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')

    def __str__(self):
        return f"{self.SAMP_ID} - Pressure: {self.CONS_INCN} Void Initial: {self.CONS_IVR}"

'''==================================== STRENGTH ===================================='''

'''==================================== TRIAXIALS ===================================='''

class TRIG(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='uu_general', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=50, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Sample type')
    SPEC_REF = models.CharField(max_length=50, blank=True, verbose_name='Specimen reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to top of specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of specimen preparation')
    TRIG_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Test type')
    TRIG_COND = models.CharField(max_length=50, blank=True, verbose_name='Sample condition')
    TRIG_REM = models.TextField(blank=True, verbose_name='Remarks on test')
    TRIG_METH = models.CharField(max_length=50, blank=True, verbose_name='Test method')
    TRIG_LAB = models.CharField(max_length=255, blank=True, verbose_name='Testing laboratory/organization')
    TRIG_CRED = models.CharField(max_length=50, blank=True, verbose_name='Accrediting body and reference number')
    TEST_STAT = models.CharField(max_length=50, blank=True, verbose_name='Test status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to base of specimen')
    TRIG_DEV = models.TextField(blank=True, verbose_name='Deviation from the procedure')

    def __str__(self):
        return f"{self.SAMP_ID} - Type: {self.TRIG_TYPE} Cond: {self.TRIG_COND} Lab: {self.TRIG_LAB}"

class TRIT(models.Model):
    SAMP_ID = models.ForeignKey(TRIG, on_delete=models.CASCADE, related_name='uu_test', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=50, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Sample type')
    SPEC_REF = models.CharField(max_length=50, blank=True, verbose_name='Specimen reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to top of test specimen')
    TRIT_TESN = models.CharField(max_length=50, blank=True, verbose_name='Triaxial test/stage reference')
    TRIT_SDIA = models.FloatField(null=True, verbose_name='Specimen diameter')
    TRIT_SLEN = models.FloatField(null=True, verbose_name='Specimen length')
    TRIT_IMC = models.FloatField(null=True, verbose_name='Initial water/moisture content')
    TRIT_FMC = models.FloatField(null=True, verbose_name='Final water/moisture content')
    TRIT_CELL = models.FloatField(null=True, verbose_name='Total cell pressure')
    TRIT_DEVF = models.FloatField(null=True, verbose_name='Corrected deviator stress at failure')
    TRIT_BDEN = models.FloatField(null=True, verbose_name='Initial bulk density')
    TRIT_DDEN = models.FloatField(null=True, verbose_name='Initial dry density')
    TRIT_STRN = models.FloatField(null=True, verbose_name='Axial strain at failure')
    TRIT_CU = models.FloatField(null=True, verbose_name='Undrained Shear Strength at failure')
    TRIT_MODE = models.CharField(max_length=50, blank=True, verbose_name='Mode of failure')
    TRIT_REM = models.TextField(blank=True, verbose_name='Comments')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')
    TRIT_FZWC = models.FloatField(null=True, verbose_name='Failure zone water content, if measured')
    TRIT_RATE = models.FloatField(null=True, verbose_name='Mean rate of shear')
    TRIT_TYPE = models.TextField(blank=True, verbose_name='Test type')          # NON-STANDARD
    TRIT_COND = models.TextField(blank=True, verbose_name='Sample condition')   # NON-STANDARD
    TRIT_SENS = models.FloatField(null=True, verbose_name='Sensitivity')        # NON-STANDARD

    def __str__(self):
        return f"{self.SAMP_ID} - Type: {self.TRIT_TYPE} Cond: {self.TRIT_COND} Su: {self.TRIT_CU} Max Dev: {self.TRIT_DEVF}"
    
class TREG(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='triaxial_general', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True)
    SAMP_TOP = models.FloatField(null=True)
    SAMP_REF = models.CharField(max_length=50, blank=True)
    SAMP_TYPE = models.CharField(max_length=50, blank=True)
    SPEC_REF = models.CharField(max_length=50, blank=True)
    SPEC_DPTH = models.FloatField(null=True)
    SPEC_DESC = models.TextField(blank=True)
    SPEC_PREP = models.TextField(blank=True)
    TREG_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Test Type')
    TREG_COND = models.CharField(max_length=50, blank=True, verbose_name='Sample Condition')
    TREG_COH = models.FloatField(null=True, verbose_name='Cohesion (kPa)')
    TREG_PHI = models.FloatField(null=True, verbose_name='Angle of Friction (°)')
    TREG_FCR = models.CharField(max_length=50, blank=True, verbose_name='Failure Criterion')
    TREG_REM = models.TextField(blank=True, verbose_name='Remarks')
    TREG_METH = models.CharField(max_length=255, blank=True, verbose_name='Test Method')
    TREG_LAB = models.CharField(max_length=255, blank=True, verbose_name='Laboratory Name')
    TREG_CRED = models.CharField(max_length=255, blank=True, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=50, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    TREG_DEV = models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')

    def __str__(self):
        return f"{self.SAMP_ID} - Type: {self.TREG_TYPE} Cond: {self.TREG_COND} Lab: {self.TREG_LAB} Phi: {self.TREG_PHI}"
    
class TRET(models.Model):
    SAMP_ID = models.ForeignKey(TREG, on_delete=models.CASCADE, related_name='triaxial_test', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=255, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to top of test specimen')
    SPEC_DESC = models.TextField(verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(verbose_name='Details of Specimen Preparation')
    TRET_TESN = models.CharField(max_length=255, verbose_name='Triaxial Test/Stage Number')
    TRET_SDIA = models.FloatField(verbose_name='Specimen Diameter')
    TRET_LEN = models.FloatField(verbose_name='Specimen Length')
    TRET_IMC = models.FloatField(verbose_name='Initial Water/Moisture Content')
    TRET_FMC = models.FloatField(verbose_name='Final Water/Moisture Content')
    TRET_BDEN = models.FloatField(verbose_name='Initial Bulk Density')
    TRET_DDEN = models.FloatField(verbose_name='Initial Dry Density')
    TRET_SAT = models.CharField(max_length=255, verbose_name='Method of Saturation')
    TRET_CONS = models.TextField(verbose_name='Details of Consolidation Stage')
    TRET_CONP = models.FloatField(verbose_name='Effective Stress at End of Consolidation')
    TRET_CELL = models.FloatField(verbose_name='Total Cell Pressure During Shearing Stage')
    TRET_PWPI = models.FloatField(verbose_name='Porewater Pressure at Start of Shear Stage')
    TRET_STRR = models.FloatField(verbose_name='Rate of Axial Strain During Shear')
    TRET_STRN = models.FloatField(verbose_name='Axial Strain at Failure')
    TRET_DEVF = models.FloatField(verbose_name='Deviator Stress at Failure')
    TRET_PWPF = models.FloatField(verbose_name='Porewater Pressure at Failure')
    TRET_STV = models.FloatField(verbose_name='Volumetric Strain at Failure (Drained Only)')
    TRET_MODE = models.CharField(max_length=255, verbose_name='Mode of Failure')
    TRET_REM = models.TextField(verbose_name='Comments')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File reference')
    TRET_BACK = models.FloatField(verbose_name='Final Back Pressure Applied Prior to Shearing')
    TRET_VERT = models.FloatField(verbose_name='Vertical Strain at End of Consolidation')
    TRET_VOLM = models.FloatField(verbose_name='Volumetric Strain at End of Consolidation')
    TRET_RATE = models.FloatField(verbose_name='Rate of Volumetric Strain Immediately Prior to Shearing')
    TRET_BVAL = models.FloatField(verbose_name='Final B-Value Prior to Shearing')
    TRET_DRN = models.CharField(max_length=255, verbose_name='Type of Drainage Conditions During Shear')
    TRET_MEMB = models.FloatField(verbose_name='Membrane Corrections Applied at Failure')
    TRET_FILC = models.FloatField(verbose_name='Filter Paper Corrections Applied at Failure')
    TRET_IVR = models.FloatField(verbose_name='Initial Voids Ratio')
    TRET_SATR = models.FloatField(verbose_name='Saturation Percentage')
    TRET_CVP = models.FloatField(verbose_name='Effective Vertical Pressure at End of Consolidation')
    TRET_CRP = models.FloatField(verbose_name='Effective Radial Pressure at End of Consolidation')
    TRET_MEAN = models.FloatField(verbose_name='Peak Mean Effective Stress During Shear')
    TRET_CU = models.FloatField(verbose_name='Undrained Shear Strength at Failure')
    TRET_EP50 = models.FloatField(verbose_name='Strain at 50% Peak Deviator Stress')
    TRET_E50 = models.FloatField(verbose_name='Secant Modulus at 50% Peak Deviator Stress')
    TRET_FVR = models.FloatField(verbose_name='Final Voids Ratio')                              # NON-STANDARD
    TRET_TYPE = models.CharField(max_length=50, blank=True, verbose_name='Test Type')           # NON-STANDARD
    TRET_COND = models.CharField(max_length=50, blank=True, verbose_name='Sample Condition')    # NON-STANDARD
    TRET_EP50 = models.FloatField(verbose_name='Epsilon 50 (%)')                                # NON-STANDARD
    TRET_K0 = models.FloatField(verbose_name='Calculated K0')                                   # NON-STANDARD
    TRET_EXPP = models.FloatField(verbose_name='Excess Pore Pressure')                          # NON-STANDARD
    TRET_MAJOR = models.FloatField(verbose_name='Major Principal Stress At Failure ')           # NON-STANDARD
    TRET_MINOR = models.FloatField(verbose_name='Minor Principal Stress At Failure ')           # NON-STANDARD
    TRET_SQ = models.FloatField(verbose_name='Sample Quality')                                  # NON-STANDARD
    TRET_QNET = models.FloatField(verbose_name='Qnet Correlation')                              # NON-STANDARD

    def __str__(self):
        return f"{self.SAMP_ID} - Type: {self.TRET_TYPE} Cond: {self.TRET_COND} Su: {self.TRET_CU} Max Dev: {self.TRET_DEVF}"
    
'''==================================== OFFSHORE STRENGTH ====================================''' 

class LPEN(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='hand_pen', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location', blank=True)
    SAMP_TOP = models.FloatField(verbose_name='Depth to top of sample', null=True)
    SAMP_REF = models.CharField(max_length=50, verbose_name='Sample reference', blank=True)
    SAMP_TYPE = models.CharField(max_length=50, verbose_name='Sample type', blank=True)
    SPEC_REF = models.CharField(max_length=50, verbose_name='Specimen reference', blank=True)
    SPEC_DPTH = models.FloatField(verbose_name='Depth to top of specimen', null=True)
    SPEC_DESC = models.TextField(verbose_name='Specimen description', blank=True)
    SPEC_PREP = models.TextField(verbose_name='Details of specimen preparation', blank=True)
    LPEN_PPEN = models.FloatField(verbose_name='Hand penetrometer undrained shear strength', null=True)
    LPEN_MC = models.FloatField(verbose_name='Water/moisture content local to test', null=True)
    LPEN_REM = models.TextField(verbose_name='Remarks', blank=True)
    LPEN_METH = models.CharField(max_length=255, verbose_name='Test method', blank=True)
    LPEN_LAB = models.CharField(max_length=255, verbose_name='Name of testing laboratory/organization', blank=True)
    LPEN_CRED = models.CharField(max_length=255, verbose_name='Accrediting body and reference number', blank=True)
    TEST_STAT = models.CharField(max_length=50, verbose_name='Test status', blank=True)
    FILE_FSET = models.CharField(max_length=255, verbose_name='File reference', blank=True)
    SPEC_BASE = models.FloatField(verbose_name='Depth to base of specimen', null=True)

    def __str__(self):
        return f"{self.SAMP_ID} - Su: {self.LPEN_PPEN} kPa"
    
class LVAN(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='lab_vane', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location', blank=True)
    SAMP_TOP = models.FloatField(verbose_name='Depth to top of sample', null=True)
    SAMP_REF = models.CharField(max_length=50, verbose_name='Sample reference', blank=True)
    SAMP_TYPE = models.CharField(max_length=50, verbose_name='Sample type', blank=True)
    SPEC_REF = models.CharField(max_length=50, verbose_name='Specimen reference', blank=True)
    SPEC_DPTH = models.FloatField(verbose_name='Depth to top of specimen', null=True)
    SPEC_DESC = models.TextField(verbose_name='Specimen description', blank=True)
    SPEC_PREP = models.TextField(verbose_name='Details of specimen preparation', blank=True)
    LVAN_VNPK = models.FloatField(verbose_name='Vane undrained shear strength (peak)', null=True)
    LVAN_VNRM = models.FloatField(verbose_name='Vane undrained shear strength (remoulded)', null=True)
    LVAN_MC = models.FloatField(verbose_name='Water/moisture content local to the test', null=True)
    LVAN_SIZE = models.FloatField(verbose_name='Equivalent diameter of vane', null=True)
    LVAN_VLEN = models.FloatField(verbose_name='Length of vane', null=True)
    LVAN_REM = models.TextField(verbose_name='Remarks', blank=True)
    LVAN_METH = models.CharField(max_length=255, verbose_name='Test method', blank=True)
    LVAN_LAB = models.CharField(max_length=255, verbose_name='Name of testing laboratory/organization', blank=True)
    LVAN_CRED = models.CharField(max_length=255, verbose_name='Accrediting body and reference number', blank=True)
    TEST_STAT = models.CharField(max_length=50, verbose_name='Test status', blank=True)
    FILE_FSET = models.CharField(max_length=255, verbose_name='File reference', blank=True)
    SPEC_BASE = models.FloatField(verbose_name='Depth to base of specimen', null=True)
    LVAN_DEV = models.TextField(verbose_name='Deviation from the specified procedure', blank=True)
    LVAN_TYPE = models.CharField(max_length=50, verbose_name='Vane type', blank=True)       # USE THIS TO REMOVE TORV GROUP

    def __str__(self):
        return f"{self.SAMP_ID} - Type: {self.LVAN_TYPE} Su: {self.LVAN_VNPK} Size: {self.LVAN_SIZE} Lab: {self.LVAN_LAB}"
    
'''==================================== BENDER ===================================='''
    
class LDYN(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='bender', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True)
    SAMP_TOP = models.FloatField(null=True)
    SAMP_REF = models.CharField(max_length=50, blank=True)
    SAMP_TYPE = models.CharField(max_length=50, blank=True)
    SPEC_REF = models.CharField(max_length=50, blank=True)
    SPEC_DPTH = models.FloatField(null=True)
    SPEC_DESC = models.TextField(blank=True)
    SPEC_PREP = models.TextField(blank=True)
    LDYN_PWAV = models.FloatField(null=True, verbose_name='P-wave velocity (m/s)')
    LDYN_SWAV = models.FloatField(null=True, verbose_name='S-wave velocity (m/s)')
    LDYN_EMOD = models.FloatField(null=True, verbose_name='Dynamic elastic modulus (GPa)')
    LDYN_SG = models.FloatField(null=True, verbose_name='Shear modulus (GPa)')
    LDYN_REM = models.TextField(blank=True, verbose_name='Remarks')
    LDYN_METH = models.CharField(max_length=255, blank=True, verbose_name='Test Method')
    LDYN_LAB = models.CharField(max_length=255, blank=True, verbose_name='Laboratory Name')
    LDYN_CRED = models.CharField(max_length=255, blank=True, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=50, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    LDYN_DEV = models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')

    def __str__(self):
        return f"{self.SAMP_ID} - SWAV: {self.LDYN_SWAV} SG: {self.LDYN_SG} Lab: {self.LDYN_LAB}"
    
'''==================================== SHEARBOX ===================================='''

class SHBG(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='shearbox_general', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=255, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to top of test specimen')
    SPEC_DESC = models.TextField(verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(verbose_name='Details of Specimen Preparation')
    SHBG_TYPE = models.CharField(max_length=255, verbose_name='Test Type')
    SHBG_COND = models.CharField(max_length=255, verbose_name='Sample Condition')
    SHBG_CONS = models.TextField(verbose_name='Specific Condition Statements')
    SHBG_PCOH = models.FloatField(verbose_name='Peak Cohesion Intercept')
    SHBG_PHI = models.FloatField(verbose_name='Peak Angle of Friction')
    SHBG_RCOH = models.FloatField(verbose_name='Residual Cohesion Intercept')
    SHBG_RPHI = models.FloatField(verbose_name='Residual Angle of Friction')
    SHBG_ENCA = models.TextField(verbose_name='Method of Encapsulation of Specimens Tested')
    SHBG_REM = models.TextField(verbose_name='Remarks')
    SHBG_METH = models.CharField(max_length=255, verbose_name='Test Method')
    SHBG_LAB = models.CharField(max_length=255, verbose_name='Name of Testing Laboratory/Organization')
    SHBG_CRED = models.CharField(max_length=255, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=255, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File reference')
    SPEC_BASE = models.FloatField(verbose_name='Depth to Base of Specimen')
    SHBG_DEV = models.TextField(verbose_name='Deviation from the Specified Procedure')

    def __str__(self):
        return f"{self.SAMP_ID} - Type: {self.SHBG_TYPE} Cond: {self.SHBG_COND} Lab: {self.SHBG_LAB} Phi: {self.SHBG_PHI}"
    
class SHBT(models.Model):
    SAMP_ID = models.ForeignKey(SHBG, on_delete=models.CASCADE, related_name='shearbox_test', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen')
    SHBT_TESN = models.CharField(max_length=255, verbose_name='Shear Box Test Stage/Specimen Reference')
    SHBT_BDEN = models.FloatField(verbose_name='Initial Bulk Density')
    SHBT_DDEN = models.FloatField(verbose_name='Initial Dry Density')
    SHBT_NORM = models.FloatField(verbose_name='Normal Stress Applied')
    SHBT_DISP = models.FloatField(verbose_name='Displacement Rate for Peak Stress Stage')
    SHBT_DISR = models.FloatField(verbose_name='Displacement Rate for Residual Stress Stage')
    SHBT_REVS = models.FloatField(verbose_name='Number of Traverses if Residual Test')
    SHBT_PEAK = models.FloatField(verbose_name='Peak Shear Stress')
    SHBT_RES = models.FloatField(verbose_name='Residual Shear Stress')
    SHBT_PDIS = models.FloatField(verbose_name='Horizontal Displacement at Peak')
    SHBT_RDIS = models.FloatField(verbose_name='Horizontal Displacement at Residual')
    SHBT_PDIN = models.FloatField(verbose_name='Vertical Displacement at Peak Shear Stress')
    SHBT_RDIN = models.FloatField(verbose_name='Vertical Displacement at Residual Shear Stress')
    SHBT_PDEN = models.FloatField(verbose_name='Particle Density')
    SHBT_IVR = models.FloatField(verbose_name='Initial Voids Ratio')
    SHBT_MCI = models.FloatField(verbose_name='Initial Water/Moisture Content')
    SHBT_MCF = models.FloatField(verbose_name='Final Water/Moisture Content')
    SHBT_DIA1 = models.FloatField(verbose_name='Specimen Diameter in Direction of Shear (Rock Joints)')
    SHBT_DIA2 = models.FloatField(verbose_name='Specimen Diameter Perpendicular to Shear (Rock Joints)')
    SHBT_HGT = models.FloatField(verbose_name='Specimen Height')
    SHBT_CRIT = models.TextField(verbose_name='Failure/Residual Strength Criterion Used')
    SHBT_REM = models.TextField(verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File reference')
    SHBT_PVST = models.FloatField(verbose_name='Normal (Vertical) Stress at Peak')
    SHBT_RVST = models.FloatField(verbose_name='Normal (Vertical) Stress at Residual')

'''==================================== ROCK ===================================='''

'''================================= POINT LOAD ===================================='''

class RPLT(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='point_load', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(verbose_name='Details of Specimen Preparation')
    RPLT_PLS = models.FloatField(verbose_name='Uncorrected Point Load (Is)')
    RPLT_PLSI = models.FloatField(verbose_name='Size Corrected Point Load Index (Is 50)')
    RPLT_PLTF = models.CharField(max_length=255, verbose_name='Point Load Test Type')
    RPLT_MC = models.FloatField(verbose_name='Water Content of Point Load Test Specimen')
    RPLT_REM = models.TextField(verbose_name='Remarks')
    RPLT_METH = models.CharField(max_length=255, verbose_name='Test Method')
    RPLT_LAB = models.CharField(max_length=255, verbose_name='Name of Testing Laboratory/Organization')
    RPLT_CRED = models.CharField(max_length=255, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=255, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference')
    SPEC_BASE = models.FloatField(verbose_name='Depth to Base of Specimen')
    RPLT_DEV = models.TextField(verbose_name='Deviation from the Specified Procedure')

    def __str__(self):
        return f"{self.SAMP_ID} - Type: {self.RPLT_PLTF} IS50: {self.RPLT_PLSI}"
    

'''================================= ROCK UCS ===================================='''

class RUCS(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='ucs', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of Specimen Preparation')
    RUCS_SDIA = models.FloatField(null=True, verbose_name='Specimen Diameter')
    RUCS_LEN = models.FloatField(null=True, verbose_name='Specimen Length')
    RUCS_MC = models.FloatField(null=True, verbose_name='Water Content of Specimen Tested')
    RUCS_COND = models.CharField(max_length=255, blank=True, verbose_name='Condition of Specimen as Tested')
    RUCS_DURN = models.CharField(max_length=255, blank=True, verbose_name='Test Duration')
    RUCS_STRA = models.FloatField(null=True, verbose_name='Stress Rate')
    RUCS_UCS = models.FloatField(null=True, verbose_name='Uniaxial Compressive Strength')
    RUCS_MODE = models.CharField(max_length=255, blank=True, verbose_name='Mode of Failure')
    RUCS_E = models.FloatField(null=True, verbose_name='Young\'s Modulus')
    RUCS_MU = models.FloatField(null=True, verbose_name='Poisson\'s Ratio')
    RUCS_ES = models.CharField(max_length=255, blank=True, verbose_name='Stress Level at Which Modulus Has Been Measured')
    RUCS_METH = models.CharField(max_length=255, blank=True, verbose_name='Test Method')
    RUCS_LAB = models.CharField(max_length=255, blank=True, verbose_name='Name of Testing Laboratory/Organization')
    RUCS_CRED = models.CharField(max_length=255, blank=True, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=255, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    RUCS_DEV = models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')
    RUCS_REM = models.TextField(blank=True, verbose_name='Remarks')
    RUCS_MACH = models.CharField(max_length=255, blank=True, verbose_name='Type of Testing Machine')
    RUCS_ESEC = models.FloatField(null=True, verbose_name='Young\'s Modulus, Secant')
    RUCS_ETAN = models.FloatField(null=True, verbose_name='Young\'s Modulus, Tangent')
    RUCS_EAVG = models.FloatField(null=True, verbose_name='Young\'s Modulus, Average')
    RUCS_SSEC = models.CharField(max_length=255, blank=True, verbose_name='Stress Level at Which Secant Young\'s Modulus Has Been Measured')
    RUCS_STAN = models.CharField(max_length=255, blank=True, verbose_name='Stress Level at Which Tangent Young\'s Modulus Has Been Measured')
    RUCS_SAVG = models.CharField(max_length=255, blank=True, verbose_name='Stress Level at Which Average Young\'s Modulus Has Been Measured')
    RUCS_MUS = models.FloatField(null=True, verbose_name='Poisson\'s Ratio, Secant')
    RUCS_MUT = models.FloatField(null=True, verbose_name='Poisson\'s Ratio, Tangent')
    RUCS_MUAV = models.FloatField(null=True, verbose_name='Poisson\'s Ratio, Average')

    def __str__(self):
        return f"{self.SAMP_ID} - UCS: {self.RUCS_UCS} MPa Young's Modulus: {self.RUCS_E} GPa Poisson's Ratio: {self.RUCS_MU}"

'''================================= ROCK MOISTURE ===================================='''

class RWCO(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='rock_moisture', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of Specimen Preparation')
    RWCO_MC = models.FloatField(verbose_name='Water Content')
    RWCO_TEMP = models.FloatField(null=True, verbose_name='Temperature Sample Dried At')
    RWCO_REM = models.TextField(blank=True, verbose_name='Remarks')
    RWCO_METH = models.CharField(max_length=255, blank=True, verbose_name='Test Method')
    RWCO_LAB = models.CharField(max_length=255, blank=True, verbose_name='Name of Testing Laboratory/Organization')
    RWCO_CRED = models.CharField(max_length=255, blank=True, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=255, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    RWCO_DEV = models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')

    def __str__(self):
        return f"{self.SAMP_ID} - Water Content: {self.RWCO_MC}%"

'''================================= ROCK DENSITY ===================================='''

class RDEN(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='rock_density', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of Specimen Preparation')
    RDEN_MC = models.FloatField(verbose_name='Water Content of Specimen')
    RDEN_SMC = models.FloatField(verbose_name='Saturated Water Content')
    RDEN_BDEN = models.FloatField(verbose_name='Bulk Density')
    RDEN_DDEN = models.FloatField(verbose_name='Dry Density')
    RDEN_PORO = models.FloatField(verbose_name='Porosity')
    RDEN_PDEN = models.FloatField(verbose_name='Apparent Particle Density')
    RDEN_TEMP = models.FloatField(null=True, verbose_name='Temperature Sample Dried At')
    RDEN_REM = models.TextField(blank=True, verbose_name='Remarks')
    RDEN_METH = models.CharField(max_length=255, blank=True, verbose_name='Test Method')
    RDEN_LAB = models.CharField(max_length=255, blank=True, verbose_name='Name of Testing Laboratory/Organization')
    RDEN_CRED = models.CharField(max_length=255, blank=True, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=255, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')
    RDEN_IDEN = models.FloatField(verbose_name='Intact Dry Density')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    RDEN_DEV = models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')

    def __str__(self):
        return f"{self.SAMP_ID} - Bulk Density: {self.RDEN_BDEN} kg/m³"

'''================================= ROCK ABRASIVE ====================================''' 

class RCAG(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='rock_abrasive_general', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Details of Specimen Preparation')
    SPEC_BASE = models.FloatField(verbose_name='Depth to Base of Specimen')
    RCAG_DEV = models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')
    RCAG_DATE = models.DateField(verbose_name='Date of Test')
    RCAG_COND = models.CharField(max_length=255, blank=True, verbose_name='Condition of Specimen as Tested')
    RCAG_GSIZ = models.FloatField(verbose_name='Maximum Grain Size')
    RCAG_ANIS = models.CharField(max_length=255, blank=True, verbose_name='Planes of Weakness or Anisotropy Present')
    RCAG_MACH = models.CharField(max_length=255, blank=True, verbose_name='Type of Apparatus')
    RCAG_MMTD = models.CharField(max_length=255, blank=True, verbose_name='Measurement Method')
    RCAG_CAIM = models.FloatField(verbose_name='CAI Mean Value')
    RCAG_CAIS = models.FloatField(verbose_name='CAI Standard Deviation')
    RCAG_ABCL = models.CharField(max_length=255, blank=True, verbose_name='Abrasiveness Classification')
    RCAG_REM = models.TextField(blank=True, verbose_name='Remarks')
    RCAG_METH = models.CharField(max_length=255, blank=True, verbose_name='Test Method')
    RCAG_LAB = models.CharField(max_length=255, blank=True, verbose_name='Name of Testing Laboratory/Organization')
    RCAG_CRED = models.CharField(max_length=255, blank=True, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=255, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')

    def __str__(self):
        return f"{self.LOCA_ID} - CAI: {self.RCAG_CAIM} Class: {self.RCAG_ABCL}"
    
class RCAT(models.Model):
    SAMP_ID = models.ForeignKey(RCAG, on_delete=models.CASCADE, related_name='rock_abrasive_test', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen')
    RCAT_TESN = models.CharField(max_length=255, blank=True, verbose_name='Measurement Number')
    RCAT_CUT = models.CharField(max_length=255, blank=True, verbose_name='Surface Condition')
    RCAT_SDIR = models.CharField(max_length=255, blank=True, verbose_name='Direction of Scratching')
    RCAT_STYH = models.FloatField(verbose_name='Rockwell Hardness HRC of Stylus')
    RCAT_STYC = models.CharField(max_length=255, blank=True, verbose_name='Stylus Condition')
    RCAT_CAI = models.FloatField(verbose_name='As Measured CAI Value')
    RCAT_CAIS = models.FloatField(verbose_name='Equivalent CAI Value')
    RCAT_REM = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')

    def __str__(self):
        return f"{self.LOCA_ID} - CAI: {self.RCAT_CAI}"

'''================================= ROCK TENSILE ===================================='''

class RTEN(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='rock_tensile', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(verbose_name='Details of Specimen Preparation')
    RTEN_SDIA = models.FloatField(verbose_name='Specimen Diameter')
    RTEN_LEN = models.FloatField(verbose_name='Specimen Thickness')
    RTEN_MC = models.FloatField(verbose_name='Water Content of Test Specimen')
    RTEN_COND = models.CharField(max_length=255, verbose_name='Condition of Specimen as Tested')
    RTEN_DURN = models.DurationField(verbose_name='Test Duration')
    RTEN_STRA = models.FloatField(verbose_name='Stress Rate')
    RTEN_TENS = models.FloatField(verbose_name='Tensile Strength')
    RTEN_MODE = models.CharField(max_length=255, verbose_name='Mode of Failure')
    RTEN_MACH = models.CharField(max_length=255, verbose_name='Testing Machine')
    RTEN_REM = models.TextField(verbose_name='Remarks')
    RTEN_METH = models.CharField(max_length=255, verbose_name='Test Method')
    RTEN_LAB = models.CharField(max_length=255, verbose_name='Name of Testing Laboratory/Organization')
    RTEN_CRED = models.CharField(max_length=255, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=255, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference')
    SPEC_BASE = models.FloatField(verbose_name='Depth to Base of Specimen')
    RTEN_DEV = models.TextField(verbose_name='Deviation from the Specified Procedure')

    def __str__(self):
        return f"{self.LOCA_ID} - Tensile Strength: {self.RTEN_TENS} MPa"

'''================================= CHALK CRUSH ===================================='''

class RCCV(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='chalk_crush', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(verbose_name='Specimen Description')
    SPEC_PREP = models.TextField(verbose_name='Details of Specimen Preparation')
    RCCV_MC = models.FloatField(verbose_name='Water Content of Specimen Tested')
    RCCV_CCV = models.FloatField(verbose_name='Chalk Crushing Value')
    RCCV_100 = models.FloatField(verbose_name='Percentage Larger Than 10mm in Original Sample')
    RCCV_REM = models.TextField(verbose_name='Remarks')
    RCCV_METH = models.CharField(max_length=255, verbose_name='Test Method')
    RCCV_LAB = models.CharField(max_length=255, verbose_name='Name of Testing Laboratory/Organization')
    RCCV_CRED = models.CharField(max_length=255, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=255, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference')
    SPEC_BASE = models.FloatField(verbose_name='Depth to Base of Specimen')
    RCCV_DEV = models.TextField(verbose_name='Deviation from the Specified Procedure')

    def __str__(self):
        return f"{self.LOCA_ID} - Crush: {self.RCCV_CCV}"

'''================================= PRESSUREMETER ===================================='''

class PMTG(models.Model):
    LOCA_ID = models.ForeignKey(LOCA, on_delete=models.CASCADE, related_name='pressuremeter_general', verbose_name='Location')

    PMTG_DPTH = models.FloatField(verbose_name='Depth of Test')
    PMTG_TESN = models.CharField(max_length=255, verbose_name='Test Reference')
    PMTG_DATE = models.DateField(verbose_name='Date of Test')
    PMTG_WAT = models.FloatField(verbose_name='Measured or Assumed Ground Water Level')
    PMTG_CONT = models.CharField(max_length=255, verbose_name='Subcontractors Name')
    PMTG_CREW = models.CharField(max_length=255, verbose_name='Operators Details')
    PMTG_REF = models.CharField(max_length=255, verbose_name='Instrument Reference / Serial Number')
    PMTG_TYPE = models.CharField(max_length=255, verbose_name='Pressuremeter Type')
    PMTG_DIAM = models.FloatField(verbose_name='Uninflated Diameter of Pressuremeter')
    PMTG_HO = models.FloatField(verbose_name='Estimated in Situ Horizontal Stress')
    PMTG_GI = models.FloatField(verbose_name='Initial Shear Modulus')
    PMTG_CU = models.FloatField(verbose_name='Undrained Shear Strength')
    PMTG_PL = models.FloatField(verbose_name='Limit Pressure')
    PMTG_AF = models.FloatField(verbose_name='Angle of Friction')
    PMTG_AD = models.FloatField(verbose_name='Angle of Dilation')
    PMTG_AFCV = models.FloatField(verbose_name='Angle of Friction at Constant Volume')
    PMTG_METH = models.TextField(verbose_name='Method(s) Used to Determine Derived Soil Parameters')
    PMTG_CRED = models.CharField(max_length=255, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=255, verbose_name='Test Status')
    PMTG_ENV = models.TextField(verbose_name='Details of Weather and Environmental Conditions During Test')
    PMTG_REM = models.TextField(verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference')
    PMTG_NUAR = models.FloatField(verbose_name='Number of Arms')
    PMTG_ORNT = models.FloatField(verbose_name='Bearing of Arm 1')
    PMTG_AXIS = models.CharField(max_length=255, verbose_name='Arm Combination Used for Analysis')

    def __str__(self):
        return f"{self.LOCA_ID} - Type: {self.PMTG_TYPE} Su: {self.PMTG_CU}"

class PMTD(models.Model):
    PMTG_TESN = models.ForeignKey(PMTG, on_delete=models.CASCADE, related_name='pressuremeter_test_id', verbose_name='Test ID')
    PMTG_DPTH = models.ForeignKey(PMTG, on_delete=models.CASCADE, related_name='pressuremeter_test_depth', verbose_name='Test ID')

    LOCA_ID = models.CharField(max_length=255, verbose_name='Location')
    PMTD_SEQ = models.FloatField(verbose_name='Sequence Number')
    PMTD_ARM1 = models.FloatField(verbose_name='Axis 1 Displacement')
    PMTD_ARM2 = models.FloatField(verbose_name='Axis 2 Displacement')
    PMTD_ARM3 = models.FloatField(verbose_name='Axis 3 Displacement')
    PMTD_TPC = models.FloatField(verbose_name='Total Pressure')
    PMTD_PPA = models.FloatField(verbose_name='Pore Pressure Cell A')
    PMTD_PPB = models.FloatField(verbose_name='Pore Pressure Cell B')
    PMTD_VOL = models.FloatField(verbose_name='Volume Change in Test Cell')
    PMTD_REM = models.TextField(verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference')
    PMTD_AX1 = models.FloatField(verbose_name='Axis 1 Displacement')
    PMTD_AX2 = models.FloatField(verbose_name='Axis 2 Displacement')
    PMTD_AX3 = models.FloatField(verbose_name='Axis 3 Displacement')
    PMTD_SA1 = models.FloatField(verbose_name='Arm 1 Displacement')
    PMTD_SA2 = models.FloatField(verbose_name='Arm 2 Displacement')
    PMTD_SA3 = models.FloatField(verbose_name='Arm 3 Displacement')
    PMTD_SA4 = models.FloatField(verbose_name='Arm 4 Displacement')
    PMTD_SA5 = models.FloatField(verbose_name='Arm 5 Displacement')
    PMTD_SA6 = models.FloatField(verbose_name='Arm 6 Displacement')
    PMTD_SAME = models.FloatField(verbose_name='Mean Arm Displacement')

class PMTL(models.Model):
    PMTG_TESN = models.OneToOneField(PMTG, on_delete=models.CASCADE, related_name='pressuremeter_loops_id', verbose_name='Test ID')
    PMTG_DPTH = models.ForeignKey(PMTG, on_delete=models.CASCADE, related_name='pressuremeter_loops_depth', verbose_name='Test ID')

    LOCA_ID = models.CharField(max_length=255, verbose_name='Location')
    PMTL_LNO = models.FloatField(verbose_name='Unload/Reload Loop Number')
    PMTL_GAA = models.FloatField(verbose_name='Unload/Reload Shear Modulus Average')
    PMTL_SINC = models.FloatField(verbose_name='Mean Strain')
    PMTL_PINC = models.FloatField(verbose_name='Mean Pressure')
    PMTL_STRA = models.FloatField(verbose_name='Strain Range or Amplitude')
    PMTL_PRSA = models.FloatField(verbose_name='Pressure Range or Amplitude')
    PMTL_NLSA = models.FloatField(verbose_name='Shear Stress Coefficient')
    PMTL_NLSB = models.FloatField(verbose_name='Linearity Exponent')
    PMTL_REM = models.TextField(verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference')
    PMTL_AXIS = models.CharField(max_length=255, verbose_name='Arm Combination Used for Analysis')

'''==================================== ADVANCED ===================================='''

'''================================ DSS (WITH CYCLIC) ===================================='''


class DSSG(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='dss_general', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, verbose_name='Location')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen')
    DSSG_TESN = models.CharField(max_length=255, verbose_name='DSS Test Number')
    SPEC_DESC = models.TextField(verbose_name='Specimen Description')
    SPEC_PREP = models.CharField(max_length=255, verbose_name='Specimen Preparation Technique')
    DSSG_COND = models.CharField(max_length=255, blank=True, verbose_name='Condition of Specimen as Tested')
    DSSG_TYPE = models.CharField(max_length=255, verbose_name='Test Type')
    DSSG_LAB = models.CharField(max_length=255, verbose_name='Name of Testing Laboratory/Organisation')
    DSSG_DESC = models.TextField(verbose_name='Description of the Test')
    DSSG_DRCO = models.CharField(max_length=255, verbose_name='Drainage Condition')
    DSSG_STRR = models.FloatField(verbose_name='Strain Rate During Shear Phase')
    DSSG_PDEN = models.FloatField(verbose_name='Particle Density')
    DSSG_EVES = models.FloatField(verbose_name='Estimated in Situ Vertical Effective Stress')
    DSSG_METH = models.CharField(max_length=255, verbose_name='Test Method')
    DSSG_CRED = models.CharField(max_length=255, verbose_name='Accrediting Body and Reference Number')
    DSSG_REM = models.TextField(verbose_name='General Remarks')
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference')
    DSSG_DMAX = models.FloatField(verbose_name='Corresponding Maximum Dry Density')
    DSSG_EMIN = models.FloatField(verbose_name='Corresponding Minimum Void Ratio')
    DSSG_DMIN = models.FloatField(verbose_name='Corresponding Minimum Dry Density')
    DSSG_EMAX = models.FloatField(verbose_name='Corresponding Maximum Void Ratio')

class DSST(models.Model):
    DSSG_TESN = models.OneToOneField(DSSG, on_delete=models.CASCADE, related_name='dss_test', verbose_name='Test number')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample type')
    SAMP_ID = models.CharField(max_length=255, blank=True, verbose_name='Sample ID')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Specimen depth')
    DSST_IDIA = models.FloatField(null=True, verbose_name='Initial sample diameter')
    DSST_ILEN = models.FloatField(null=True, verbose_name='Initial sample height')
    DSST_IMC = models.FloatField(null=True, verbose_name='Initial water/moisture content')
    DSST_ITDE = models.FloatField(null=True, verbose_name='Initial bulk density')
    DSST_IDDE = models.FloatField(null=True, verbose_name='Initial dry density')
    DSST_ISAT = models.FloatField(null=True, verbose_name='Initial degree of saturation')
    DSST_IVR = models.FloatField(null=True, verbose_name='Initial void ratio')
    DSST_IID = models.FloatField(null=True, verbose_name='Initial relative density')
    DSST_PPCP = models.FloatField(null=True, verbose_name='Pre-consolidation pressure used for pre-loading')
    DSST_PMVS = models.FloatField(null=True, verbose_name='Max vertical effective stress during pre-loading')
    DSST_CMC = models.FloatField(null=True, verbose_name='Post-consolidation moisture content')
    DSST_CTDE = models.FloatField(null=True, verbose_name='Post-consolidation bulk density')
    DSST_CDDE = models.FloatField(null=True, verbose_name='Post-consolidation dry density')
    DSST_CSAT = models.FloatField(null=True, verbose_name='Post-consolidation degree of saturation')
    DSST_CVR = models.FloatField(null=True, verbose_name='Post-consolidation voids ratio')
    DSST_CID = models.FloatField(null=True, verbose_name='Post-consolidation relative density')
    DSST_CEFF = models.FloatField(null=True, verbose_name='Post-consolidation vertical effective stress')
    DSST_CAST = models.FloatField(null=True, verbose_name='Post-consolidation vertical strain')
    DSST_CVST = models.FloatField(null=True, verbose_name='Post-consolidation volumetric strain')
    DSST_CSQ = models.CharField(max_length=255, blank=True, verbose_name='Sample quality in accordance with method described in Lunne et al. (2006), i.e. Δe/e0')
    DSST_FMC = models.FloatField(null=True, verbose_name='Moisture content at failure')
    DSST_FTDE = models.FloatField(null=True, verbose_name='Bulk density at failure')
    DSST_FDDE = models.FloatField(null=True, verbose_name='Dry density at failure')
    DSST_FSAT = models.FloatField(null=True, verbose_name='Degree of saturation at failure')
    DSST_FVR = models.FloatField(null=True, verbose_name='Void ratio at failure')
    DSST_FSHS = models.FloatField(null=True, verbose_name='Shear stress at failure')
    DSST_FNMP = models.FloatField(null=True, verbose_name='Normal stress at failure')
    DSST_FAST = models.FloatField(null=True, verbose_name='Vertical strain at failure')
    DSST_FVST = models.FloatField(null=True, verbose_name='Volumetric strain at failure')
    DSST_FSST = models.FloatField(null=True, verbose_name='Shear strain at failure')
    DSST_FCPP = models.FloatField(null=True, verbose_name='Inferred pore pressure at failure')
    DSST_FSM = models.FloatField(null=True, verbose_name='Secant shear modulus at failure')

    DSST_PRDE = models.TextField(blank=True, verbose_name='Description of pre-shearing process')        # CYCLIC SHEARING FIELDS START
    DSST_PRCS = models.FloatField(null=True, verbose_name='Cyclic shear stress during pre-shearing')
    DSST_PRCN = models.FloatField(null=True, verbose_name='Number of cycles during pre-shearing')
    DSST_PRMS = models.FloatField(null=True, verbose_name='Vertical effective stress during pre-shearing')
    DSST_CSR = models.FloatField(null=True, verbose_name='Cyclic stress ratio')
    DSST_FRS = models.FloatField(null=True, verbose_name='Reference stress')
    DSST_CFRQ = models.FloatField(null=True, verbose_name='Cycle frequency')
    DSST_FAAS = models.FloatField(null=True, verbose_name='Average shear stress at failure')
    DSST_FSSA = models.FloatField(null=True, verbose_name='Cyclic shear stress at failure')
    DSST_FCTF = models.FloatField(null=True, verbose_name='Total number of cycles at failure')
    DSST_FASS = models.FloatField(null=True, verbose_name='Average shear strain at failure')
    DSST_FPSS = models.FloatField(null=True, verbose_name='Permanent shear strain at failure')
    DSST_FCSS = models.FloatField(null=True, verbose_name='Cyclic shear strain at failure')
    DSST_FPPR = models.FloatField(null=True, verbose_name='Permanent excess pore pressure ratio at failure')
    DSST_PP10 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 10% permanent excess pore pressure ratio')
    DSST_PP20 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 20% permanent excess pore pressure ratio')
    DSST_PP30 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 30% permanent excess pore pressure ratio')
    DSST_PP40 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 40% permanent excess pore pressure ratio')
    DSST_PP50 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 50% permanent excess pore pressure ratio')
    DSST_PP60 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 60% permanent excess pore pressure ratio')
    DSST_PP70 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 70% permanent excess pore pressure ratio')
    DSST_PP80 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 80% permanent excess pore pressure ratio')
    DSST_PP90 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 90% permanent excess pore pressure ratio')
    DSST_PPMX = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 97.5% permanent excess pore pressure ratio')
    DSST_SS01 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 1(%) cyclic shear strain')
    DSST_SS02 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 2(%) cyclic shear strain')
    DSST_SS05 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 5(%) cyclic shear strain')
    DSST_SS10 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 10(%) cyclic shear strain')
    DSST_SS15 = models.FloatField(null=True, verbose_name='Number of cycles taken to accumulate 15(%) cyclic shear strain')
    DSST_GP10 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at permanent excess pore water pressure of 10%')
    DSST_GP20 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at permanent excess pore water pressure of 20%')
    DSST_GP30 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at permanent excess pore water pressure of 30%')
    DSST_GP40 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at permanent excess pore water pressure of 40%')
    DSST_GP50 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at permanent excess pore water pressure of 50%')
    DSST_GP60 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at permanent excess pore water pressure of 60%')
    DSST_GP70 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at permanent excess pore water pressure of 70%')
    DSST_GP80 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at permanent excess pore water pressure of 80%')
    DSST_GP90 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at permanent excess pore water pressure of 90%')
    DSST_GPMX = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at permanent excess pore water pressure of 97.5%')
    DSST_GS01 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at cyclic shear strain of 1%')
    DSST_GS02 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at cyclic shear strain of 2%')
    DSST_GS05 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at cyclic shear strain of 5%')
    DSST_GS10 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at cyclic shear strain of 10%')
    DSST_GS15 = models.FloatField(null=True, verbose_name='Normalised secant shear modulus (GN/G1) at cyclic shear strain of 15%')
    DSST_REM = models.TextField(blank=True, verbose_name='General remarks and observations associated with the test')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference (e.g. ASCII .csv file containing logged instrumentation data)')

    def __str__(self):
        return f"{self.SAMP_ID} - Test Number: {self.DSSG_TESN}"
    
'''================================= RING SHEAR ===================================='''

class IRSG(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='ring_shear_general', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample type')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to top of test specimen')
    IRSG_TESN = models.CharField(max_length=255, blank=True, verbose_name='Interface ring shear test number')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Geological description of the specimen')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Specimen preparation / reconstitution technique')
    IRSG_COND = models.CharField(max_length=255, blank=True, verbose_name='Condition of Specimen as Tested')
    IRSG_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Test apparatus')
    IRSG_LAB = models.CharField(max_length=255, blank=True, verbose_name='Testing laboratory')
    IRSG_EVES = models.FloatField(null=True, verbose_name='Estimated in situ vertical effective stress')
    IRSG_DRCO = models.CharField(max_length=255, blank=True, verbose_name='Drainage condition')
    IRSG_RCLA = models.FloatField(null=True, verbose_name='Center line average roughness, RCLA')
    IRSG_RSLW = models.FloatField(null=True, verbose_name='Rate of slow shearing impulse')
    IRSG_RFST = models.FloatField(null=True, verbose_name='Rate of fast shearing impulse')
    IRSG_DESM = models.TextField(blank=True, verbose_name='Related design methods')
    IRSG_METH = models.CharField(max_length=255, blank=True, verbose_name='Test method')
    IRSG_CRED = models.CharField(max_length=255, blank=True, verbose_name='Accrediting body and reference number')
    IRSG_REM = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')

    def __str__(self):
        return f"{self.SAMP_ID} - Test Number: {self.IRSG_TESN}"
    
class IRST(models.Model):
    IRSG_TESN = models.OneToOneField(IRSG, on_delete=models.CASCADE, related_name='ring_shear_test', verbose_name='Test ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample type')
    SAMP_ID = models.CharField(max_length=255, blank=True, verbose_name='Sample ID')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to top of test specimen')
    IRST_ODIA = models.FloatField(null=True, verbose_name='Outer diameter of specimen')
    IRST_IDIA = models.FloatField(null=True, verbose_name='Inner diameter of specimen')
    IRST_HIGT = models.FloatField(null=True, verbose_name='Height of specimen')
    IRST_IMC = models.FloatField(null=True, verbose_name='Initial moisture content')
    IRST_IFNS = models.FloatField(null=True, verbose_name='Normal stress prior to fast shearing (consolidation stage 1)')
    IRST_ISNS = models.FloatField(null=True, verbose_name='Normal stress prior to slow shearing (consolidation stage 1)')
    IRST_COVD = models.FloatField(null=True, verbose_name='Vertical displacement during consolidation')
    IRST_FMC = models.FloatField(null=True, verbose_name='Final water/moisture content')
    IRST_FFTD = models.FloatField(null=True, verbose_name='Total shearing displacement during fast impulse shearing')
    IRST_FFNP = models.IntegerField(blank=True, null=True, verbose_name='Number of fast shearing pulses')
    IRST_FFPP = models.IntegerField(blank=True, null=True, verbose_name='Pause period between fast impulses')
    IRST_FFTH = models.FloatField(null=True, verbose_name='Total height change during fast shearing')
    IRST_FSTD = models.FloatField(null=True, verbose_name='Total shearing displacement during slow impulse shearing')
    IRST_FSTH = models.FloatField(null=True, verbose_name='Total height change during slow shearing')
    IRST_FPEA = models.FloatField(null=True, verbose_name='Peak shear stress')
    IRST_RSHS = models.FloatField(null=True, verbose_name='Residual shear stress')
    IRST_PSSD = models.FloatField(null=True, verbose_name='Displacement at peak shear stress')
    IRST_RSSD = models.FloatField(null=True, verbose_name='Displacement at residual shear stress')
    IRST_FA10 = models.FloatField(null=True, verbose_name='Average interface friction angle at 10 mm (±0.5 mm)')
    IRST_SPHI = models.FloatField(null=True, verbose_name='Peak interface friction angle from slow shearing stage')
    IRST_SRPH = models.FloatField(null=True, verbose_name='Residual interface friction angle from slow shearing stage')
    IRST_FPHI = models.FloatField(null=True, verbose_name='Peak interface friction angle from fast shearing stage')
    IRST_FRPH = models.FloatField(null=True, verbose_name='Residual interface friction angle from fast shearing stage')
    IRST_REM = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')
    IRST_FULT = models.FloatField(null=True, verbose_name='Ultimate Interface Friction Angle')       # NON-STANDARD

    def __str__(self):
        return f"{self.SAMP_ID} - Residual shear stress: {self.IRST_RSHS} Residual Phi Slow: {self.IRST_SRPH} Residual Phi Fast: {self.IRST_FRPH}"
    
    def get_ultimate(self):
        return f"{self.SAMP_ID} - Ultimate Interface Friction Angle: {self.IRST_FULT}"

class IRSV(models.Model):
    IRSG_TESN = models.OneToOneField(IRSG, on_delete=models.CASCADE, related_name='ring_shear_values', verbose_name='Test ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample type')
    SAMP_ID = models.CharField(max_length=255, blank=True, verbose_name='Sample ID')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to top of test specimen')
    IRSV_TESP = models.CharField(max_length=255, blank=True, verbose_name='Test phase')
    IRSV_DATP = models.CharField(max_length=255, blank=True, verbose_name='Data point')
    IRSV_DISP = models.FloatField(null=True, verbose_name='Measured shear displacement')
    IRSV_SRTM = models.FloatField(null=True, verbose_name='Square root time')
    IRSV_AXLD = models.FloatField(null=True, verbose_name='Axial load')
    IRSV_AXDP = models.FloatField(null=True, verbose_name='Axial displacement')
    IRSV_AXST = models.FloatField(null=True, verbose_name='Axial strain')
    IRSV_SHS = models.FloatField(null=True, verbose_name='Shear stress')
    IRSV_SHDP = models.FloatField(null=True, verbose_name='Shear displacement/Horizontal displacement')
    IRSV_REM = models.TextField(blank=True, verbose_name='Remarks')

    def __str__(self):
        return f"{self.IRSG_TESN} - Phase: {self.IRSV_TESP} - Data Point: {self.IRSV_DATP}"

'''================================= RESONANT COLUMN ===================================='''

class RESG(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='res_col_general', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample type')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to top of test specimen')
    RESG_TESN = models.CharField(max_length=255, blank=True, verbose_name='Resonant column test number')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Geological description of the specimen')
    SPEC_PREP = models.TextField(blank=True, verbose_name='Specimen preparation / reconstitution technique')
    RESG_COND = models.CharField(max_length=255, blank=True, verbose_name='Condition of Specimen as Tested')
    RESG_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Test apparatus')
    RESG_LAB = models.CharField(max_length=255, blank=True, verbose_name='Name of testing laboratory/organisation')
    RESG_ORI = models.CharField(max_length=255, blank=True, verbose_name='Sample orientation')
    RESG_EVES = models.FloatField(null=True, verbose_name='Estimated in situ vertical effective stress')
    RESG_METH = models.CharField(max_length=255, blank=True, verbose_name='Test method')
    RESG_CRED = models.CharField(max_length=255, blank=True, verbose_name='Accrediting body and reference number')
    RESG_REM = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')

    def __str__(self):
        return f"{self.SAMP_ID} - Cond: {self.RESG_COND} Lab: {self.RESG_LAB}"
    
class REST(models.Model):
    RESG_TESN = models.OneToOneField(RESG, on_delete=models.CASCADE, related_name='res_col_test', verbose_name='Test ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample type')
    SAMP_ID = models.CharField(max_length=255, blank=True, verbose_name='Sample ID')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to top of test specimen')
    REST_IMC = models.FloatField(null=True, verbose_name='Initial moisture content')
    REST_IDIA = models.FloatField(null=True, verbose_name='Initial sample diameter')
    REST_ILEN = models.FloatField(null=True, verbose_name='Initial sample length')
    REST_ITDE = models.FloatField(null=True, verbose_name='Initial bulk density')
    REST_IDDE = models.FloatField(null=True, verbose_name='Initial dry density')
    REST_IVR = models.FloatField(null=True, verbose_name='Initial void ratio')
    REST_ISAT = models.FloatField(null=True, verbose_name='Initial degree of saturation')
    REST_SBVA = models.FloatField(null=True, verbose_name='Post-saturation Skempton B-value')
    REST_SBAC = models.FloatField(null=True, verbose_name='Post-saturation back pressure')
    REST_SEAS = models.FloatField(null=True, verbose_name='Post-saturation effective axial stress')
    REST_SERS = models.FloatField(null=True, verbose_name='Post-saturation effective radial stress')
    REST_CMC = models.FloatField(null=True, verbose_name='Post-consolidation moisture content')
    REST_CTDE = models.FloatField(null=True, verbose_name='Post-consolidation bulk density')
    REST_CDDE = models.FloatField(null=True, verbose_name='Post-consolidation dry density')
    REST_CSAT = models.FloatField(null=True, verbose_name='Post-consolidation degree of saturation')
    REST_CID = models.FloatField(null=True, verbose_name='Post-consolidation relative density')
    REST_CVR = models.FloatField(null=True, verbose_name='Post-consolidation voids ratio')
    REST_CEAS = models.FloatField(null=True, verbose_name='Post-consolidation effective axial stress')
    REST_CERS = models.FloatField(null=True, verbose_name='Post-consolidation effective radial stress')
    REST_CAST = models.FloatField(null=True, verbose_name='Post-consolidation axial strain')
    REST_CVST = models.FloatField(null=True, verbose_name='Post-consolidation volumetric strain')
    REST_CPWP = models.FloatField(null=True, verbose_name='Post-consolidation pore pressure')
    REST_FTDE = models.FloatField(null=True, verbose_name='Final shear/resonance bulk density')
    REST_FDDE = models.FloatField(null=True, verbose_name='Final shear/resonance dry density')
    REST_FVR = models.FloatField(null=True, verbose_name='Final shear/resonance void ratio')
    REST_FSST = models.FloatField(null=True, verbose_name='Final shear/resonance maximum shear strain')
    REST_FVST = models.FloatField(null=True, verbose_name='Final shear/resonance maximum volumetric strain')
    REST_FDAM = models.FloatField(null=True, verbose_name='Final shear/resonance maximum damping')
    REST_FSMR = models.FloatField(null=True, verbose_name='Final shear/resonance normalised shear modulus by maximum shear modulus')
    REST_FNDA = models.FloatField(null=True, verbose_name='Final shear/resonance normalised damping')
    REST_FG = models.FloatField(null=True, verbose_name='Final shear/resonance maximum small strain shear modulus')
    REST_FGST = models.FloatField(null=True, verbose_name='Final shear/resonance shear strain at maximum small strain shear modulus')
    REST_SWVL = models.FloatField(null=True, verbose_name='Final shear/resonance maximum shear wave velocity')
    REST_FTIM = models.FloatField(null=True, verbose_name='Final shear/resonance elapsed time')
    REST_REM = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File reference')

    def __str__(self):
        return f"{self.SAMP_ID} - Test Number: {self.RESG_TESN}"

class RESV(models.Model):
    RESG_TESN = models.OneToOneField(RESG, on_delete=models.CASCADE, related_name='res_col_values', verbose_name='Test ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to top of sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample type')
    SAMP_ID = models.CharField(max_length=255, blank=True, verbose_name='Sample ID')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to top of test specimen')
    RESV_DATP = models.IntegerField(null=True, verbose_name='Data point')
    RESV_RCSS = models.FloatField(null=True, verbose_name='Final shear/resonance shear strain')
    RESV_RCSM = models.FloatField(null=True, verbose_name='Final shear/resonance small strain shear modulus')
    RESV_RCDR = models.FloatField(null=True, verbose_name='Final shear/resonance damping ratio')

    def __str__(self):
        return f"{self.SAMP_ID} - Index: {self.RESV_DATP} Shear Strain: {self.RESV_DATP}"

'''================================= CYCLIC ===================================='''

class CTRG(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='cyclic_general', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    SPEC_DESC = models.TextField(blank=True, verbose_name='Specimen Description')
    SPEC_PREP = models.CharField(max_length=255, blank=True, verbose_name='Specimen Preparation Technique Used')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    CTRG_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Type of Test')
    CTRG_MCI = models.FloatField(null=True, verbose_name='Initial Water/Moisture Content')
    CTRG_MCF = models.FloatField(null=True, verbose_name='Final Water/Moisture Content')
    CTRG_H2O = models.TextField(blank=True, verbose_name='Description of Water Used for Filter Flushing')
    CTRG_SBP = models.FloatField(null=True, verbose_name='Saturation Back Pressure')
    CTRG_SATR = models.FloatField(null=True, verbose_name='Initial Degree of Saturation after Back Pressure')
    CTRG_IRD = models.FloatField(null=True, verbose_name='Initial Sample Relative Density')
    CTRG_SDIA = models.FloatField(null=True, verbose_name='Initial Specimen Diameter')
    CTRG_HIGT = models.FloatField(null=True, verbose_name='Initial Height of Specimen')
    CTRG_TMSS = models.FloatField(null=True, verbose_name='Total Mass of Installed Specimen')
    CTRG_PDEN = models.FloatField(null=True, verbose_name='Particle Density (if value assumed, prefix with #)')
    CTRG_MADD = models.FloatField(null=True, verbose_name='Maximum Density of Sand')
    CTRG_MIDD = models.FloatField(null=True, verbose_name='Minimum Density of Sand')
    CTRG_DDEN = models.FloatField(null=True, verbose_name='Initial Dry Density')
    CTRG_BDEN = models.FloatField(null=True, verbose_name='Initial Bulk Density')
    CTRG_IVR = models.FloatField(null=True, verbose_name='Initial Voids Ratio')
    CTRG_SAT = models.CharField(max_length=255, blank=True, verbose_name='Method of Saturation')
    CTRG_DURN = models.CharField(max_length=255, blank=True, verbose_name='Test Duration')
    CTRG_REM = models.TextField(blank=True, verbose_name='Remarks')
    CTRG_METH = models.CharField(max_length=255, blank=True, verbose_name='Test Method')
    CTRG_DEV = models.TextField(blank=True, verbose_name='Deviations from the Test Method')
    CTRG_LAB = models.CharField(max_length=255, blank=True, verbose_name='Testing Laboratory/Organization')
    CTRG_CRED = models.CharField(max_length=255, blank=True, verbose_name='Accrediting Body and Reference Number')
    TEST_STAT = models.CharField(max_length=255, blank=True, verbose_name='Test Status')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')

    def __str__(self):
        return f"{self.SAMP_ID} - Type: {self.CTRG_TYPE} Lab: {self.CTRG_LAB}"
    
class CTRS(models.Model):
    SAMP_ID = models.ForeignKey(CTRG, on_delete=models.CASCADE, related_name='cyclic_saturation', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    CTRS_TESN = models.IntegerField(verbose_name='Test / Stage Number')
    CTRS_CELL = models.FloatField(null=True, verbose_name='Saturation Cell Pressure')
    CTRS_BPWP = models.FloatField(null=True, verbose_name='Saturation Base Porewater Pressure')
    CTRS_MPWP = models.FloatField(null=True, verbose_name='Saturation Mid-height Porewater Pressure')
    CTRS_MPB = models.FloatField(null=True, verbose_name='Saturation Mid-height B Value')
    CTRS_BB = models.FloatField(null=True, verbose_name='Saturation Base B Value')
    CTRS_SAT = models.CharField(max_length=255, blank=True, verbose_name='Saturation Method')
    CTRS_FSAT = models.CharField(max_length=255, blank=True, verbose_name='Final Saturation')
    CTRS_REM = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')

    def __str__(self):
        return f"{self.SAMP_ID} - {self.CTRS_TESN} - {self.CTRS_SAT}"
    
class CTRC(models.Model):
    SAMP_ID = models.ForeignKey(CTRG, on_delete=models.CASCADE, related_name='cyclic_consolidation', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    CTRC_TESN = models.IntegerField(verbose_name='Test / Stage Number')
    CTRC_CELL = models.FloatField(null=True, verbose_name='Final Cell Pressure')
    CTRC_BPWP = models.FloatField(null=True, verbose_name='Base Porewater Pressure')
    CTRC_MPWP = models.FloatField(null=True, verbose_name='Mid-height Porewater Pressure')
    CTRC_MPB = models.FloatField(null=True, verbose_name='Mid-height B Value')
    CTRC_BB = models.FloatField(null=True, verbose_name='Base B Value')
    CTRC_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Type of Consolidation')
    CTRC_BACF = models.FloatField(null=True, verbose_name='Final Back Pressure')
    CTRC_ELAP = models.IntegerField(verbose_name='Duration of Test/Stage Number')
    CTRC_CHGT = models.FloatField(null=True, verbose_name='Specimen Height at End of Stage')
    CTRC_DIAE = models.FloatField(null=True, verbose_name='Specimen Diameter at End of Stage')
    CTRC_MCE = models.FloatField(null=True, verbose_name='Water Content at End of Stage')
    CTRC_BDE = models.FloatField(null=True, verbose_name='Bulk Density at End of Stage')
    CTRC_DDE = models.FloatField(null=True, verbose_name='Dry Density at End of Stage')
    CTRC_RDE = models.FloatField(null=True, verbose_name='Relative Density Index of Sand at End of Stage')
    CTRC_INCE = models.FloatField(null=True, verbose_name='Voids Ratio at End of Stage')
    CTRC_ASE = models.FloatField(null=True, verbose_name='Effective Axial Stress at End of Stage')
    CTRC_RSE = models.FloatField(null=True, verbose_name='Effective Radial Stress at End of Stage')
    CTRC_SSE = models.FloatField(null=True, verbose_name='Shear Stress at End of Stage')
    CTRC_DEVE = models.FloatField(null=True, verbose_name='Deviatoric Stress at End of Stage')
    CTRC_MNSE = models.FloatField(null=True, verbose_name='Mean Effective Stress at End of Stage')
    CTRC_RTOE = models.FloatField(null=True, verbose_name='Ratio of Radial to Axial Effective Stress at End of Stage')
    CTRC_EASE = models.FloatField(null=True, verbose_name='External Axial Strain at End of Stage')
    CTRC_VLSE = models.FloatField(null=True, verbose_name='Volumetric Strain from Measured Volume Change at End of Stage')
    CTRC_RDSE = models.FloatField(null=True, verbose_name='Radial Strain from Measured Volume Change at End of Stage')
    CTRC_B = models.FloatField(null=True, verbose_name='B Value')
    CTRC_BETS = models.CharField(max_length=255, blank=True, verbose_name='Bender Element Test Sequence')
    CTRC_BEAX = models.CharField(max_length=255, blank=True, verbose_name='Bender Element Axis of Measurement')
    CTRC_BEDS = models.FloatField(null=True, verbose_name='Distance Between Bender Elements')
    CTRC_MAT = models.FloatField(null=True, verbose_name='Measured Arrival Time of Propagated Wave')
    CTRC_MATM = models.CharField(max_length=255, blank=True, verbose_name='Method of Measuring Arrival Time')
    CTRC_SWV = models.FloatField(null=True, verbose_name='Calculated Shear Wave Velocity')
    CTRC_SMGM = models.FloatField(null=True, verbose_name='Shear Modulus Gmax')
    CTRC_REM = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')

    def __str__(self):
        return f"{self.SAMP_ID}: {self.CTRC_TYPE}"

class CTRP(models.Model):
    CTRC_TESN = models.ForeignKey(CTRC, on_delete=models.CASCADE, related_name='cyclic_derived', verbose_name='Test / Stage Number')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample Type')
    SAMP_ID = models.CharField(max_length=255, blank=True, verbose_name='Sample Unique Identifier')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    CTRP_CYC = models.IntegerField(verbose_name='Cycle Number')
    CTRP_CYCF = models.IntegerField(verbose_name='Cycle Number of Failure')
    CTRP_PWPM = models.FloatField(null=True, verbose_name='Maximum Excess Porewater Pressure')
    CTRP_MNPP = models.FloatField(null=True, verbose_name='Minimum Excess Porewater Pressure')
    CTRP_MXSS = models.FloatField(null=True, verbose_name='Maximum Shear Stress')
    CTRP_MNSS = models.FloatField(null=True, verbose_name='Minimum Shear Stress')
    CTRP_AVSS = models.FloatField(null=True, verbose_name='Mean Shear Stress')
    CTRP_CSS = models.FloatField(null=True, verbose_name='Cyclic Shear Stress ((Max-Min)/2)')
    CTRP_ACVS = models.FloatField(null=True, verbose_name='Average Cyclic Axial Stress')
    CTRP_ASF = models.FloatField(null=True, verbose_name='Axial Strain at Failure')
    CTRP_FPWP = models.FloatField(null=True, verbose_name='Porewater Pressure at Failure')
    CTRP_QMAX = models.FloatField(null=True, verbose_name='Maximum Deviatoric Stress')
    CTRP_QMIN = models.FloatField(null=True, verbose_name='Minimum Deviatoric Stress')
    CTRP_MNES = models.FloatField(null=True, verbose_name='Mean Effective Stress at End of CTRD_CYC')
    CTRP_EAMX = models.FloatField(null=True, verbose_name='Maximum Axial Strain')
    CTRP_EAMN = models.FloatField(null=True, verbose_name='Minimum Axial Strain')
    CTRP_FVR = models.FloatField(null=True, verbose_name='Final Voids Ratio')
    CTRP_QEMX = models.FloatField(null=True, verbose_name='Deviatoric Stress at Maximum Axial Strain')
    CTRP_QEMN = models.FloatField(null=True, verbose_name='Deviatoric Stress at Minimum Axial Strain')
    CTRP_ESEC = models.FloatField(null=True, verbose_name='Secant Modulus')
    CTRP_DAMP = models.FloatField(null=True, verbose_name='Damping Ratio')
    CTRP_MODE = models.CharField(max_length=255, blank=True, verbose_name='Mode of Failure')
    CTRP_DIPL = models.FloatField(null=True, verbose_name='Percent Difference from Programmed Load')
    CTRP_OBP = models.TextField(blank=True, verbose_name='Observed Performance (Visual)')
    CTRP_REM = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')

    def __str__(self):
        return f"{self.SAMP_ID}: Cycle {self.CTRP_CYC} - {self.CTRP_MODE}"
    
class CTRD(models.Model):
    CTRC_TESN = models.ForeignKey(CTRC, on_delete=models.CASCADE, related_name='cyclic_test_data', verbose_name='Test / Stage Number')
    CTRP_CYC = models.ForeignKey(CTRP, on_delete=models.CASCADE, related_name='cyclic_cycle_data', verbose_name='Cycle Number')

    LOCA_ID = models.CharField(max_length=255, blank=True, verbose_name='Location')
    SAMP_TOP = models.FloatField(null=True, verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=255, blank=True, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=255, blank=True, verbose_name='Sample Type')
    SAMP_ID = models.CharField(max_length=255, blank=True, verbose_name='Sample Unique Identifier')
    SPEC_REF = models.CharField(max_length=255, blank=True, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(null=True, verbose_name='Depth to Top of Test Specimen')
    CTRD_TIME = models.DateTimeField(verbose_name='Date/Time of Reading')
    CTRD_COND = models.TextField(blank=True, verbose_name='Test Conditions')
    CTRD_SDIA = models.FloatField(null=True, verbose_name='Specimen Diameter')
    CTRD_HIGH = models.FloatField(null=True, verbose_name='Specimen Height')
    CTRD_CELL = models.FloatField(null=True, verbose_name='Cell Pressure')
    CTRD_BPWP = models.FloatField(null=True, verbose_name='Base Porewater Pressure')
    CTRD_MPWP = models.FloatField(null=True, verbose_name='Mid-plane Porewater Pressure')
    CTRD_EAS = models.FloatField(null=True, verbose_name='External Axial Strain')
    CTRD_LAS1 = models.FloatField(null=True, verbose_name='Local Axial Strain 1')
    CTRD_LAS2 = models.FloatField(null=True, verbose_name='Local Axial Strain 2')
    CTRD_VOL = models.FloatField(null=True, verbose_name='Volumetric Strain')
    CTRD_RAD = models.FloatField(null=True, verbose_name='Radial Strain')
    CTRD_SHSN = models.FloatField(null=True, verbose_name='Shear Strain')
    CTRD_SHST = models.FloatField(null=True, verbose_name='Shear Stress')
    CTRD_DEV = models.FloatField(null=True, verbose_name='Deviatoric Stress')
    CTRD_PSD = models.FloatField(null=True, verbose_name='Principal Stress Difference')
    CTRD_MEES = models.FloatField(null=True, verbose_name='Mean Effective Stress')
    CTRD_SECE = models.FloatField(null=True, verbose_name='Secant Young\'s Modulus (Local)')
    CTRD_TANE = models.FloatField(null=True, verbose_name='Tangent Young\'s Modulus')
    CTRD_FREQ = models.FloatField(null=True, verbose_name='Loading Frequency')
    CTRD_CSTS = models.FloatField(null=True, verbose_name='Cyclic Amplitude')
    CTRD_ACVS = models.FloatField(null=True, verbose_name='Average Cyclic Axial Stress')
    CTRD_DAVS = models.FloatField(null=True, verbose_name='Double Amplitude Axial Strain')
    CTRD_CESR = models.FloatField(null=True, verbose_name='Compression/Extension Stress Ratio')
    CTRD_EMPR = models.FloatField(null=True, verbose_name='Excess Mid-plane Pore Pressure Ratio')
    CTRD_EBPR = models.FloatField(null=True, verbose_name='Excess Base Pore Pressure Ratio')
    CTRD_REM = models.TextField(blank=True, verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='File Reference')

    def __str__(self):
        return f"{self.SAMP_ID} - id: {self.CTRC_TESN} Cycle {self.CTRP_CYC} Cond: {self.CTRD_COND}"