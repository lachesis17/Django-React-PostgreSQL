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
    PROJ_ID = models.CharField(max_length=50, primary_key=True, verbose_name='Project Identifier')
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
    PROJ_ID = models.ForeignKey(PROJ, on_delete=models.CASCADE, related_name='locations',verbose_name='Project Identifier')

    LOCA_ID = models.CharField(max_length=50, primary_key=True, verbose_name='Location Identifier')
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
    LOCA_ID = models.ForeignKey(LOCA, on_delete=models.CASCADE, related_name='samples')

    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample')
    SAMP_REF = models.CharField(max_length=50, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, verbose_name='Sample Type')
    SAMP_ID = models.CharField(max_length=50, primary_key=True, verbose_name='Sample Unique Identifier')
    SAMP_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Sample')
    SAMP_DTIM = models.DateTimeField(blank=True, verbose_name='Date and Time Sample Taken')
    SAMP_UBLO = models.IntegerField(null=True, verbose_name='Number of Blows Required to Drive Sampler')
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
    
'''==================================== GEOLOGY ===================================='''

class GEOL(models.Model):
    LOCA_ID = models.ForeignKey(LOCA, on_delete=models.CASCADE, related_name='geology_descriptions', verbose_name='Location Identifier')

    GEOL_TOP = models.FloatField(verbose_name='Depth to the Top of Stratum (m)')
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
    LOCA_ID = models.ForeignKey(LOCA, on_delete=models.CASCADE, related_name='depth_remarks', verbose_name='Location Identifier')

    DREM_TOP = models.FloatField(verbose_name='Depth to the Top of Stratum (m)')
    DREM_BASE = models.FloatField(verbose_name='Depth to the Base of Description (m)')
    DREM_REM = models.TextField(verbose_name='Remarks', blank=True)
    FILE_FSET = models.CharField(max_length=255, verbose_name='File Reference', blank=True)

    def __str__(self):
        return f"{self.LOCA_ID} - {self.DREM_REM}"
    
    def get_layers(self):
        return f"Loca: {self.LOCA_ID} Top: {self.DREM_TOP} Bot: {self.DREM_BASE} Desc: {self.DREM_REM}"
    
'''==================================== CPT DATA ===================================='''

class SCPG(models.Model):
    LOCA_ID = models.ForeignKey(LOCA, on_delete=models.CASCADE, related_name='cone_penetration_tests')

    SCPG_TESN = models.CharField(max_length=50, primary_key=True, verbose_name='Test Reference or Push Number')
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
    SCPG_TESN = models.ForeignKey('SCPG', on_delete=models.CASCADE, related_name='cone_id', verbose_name='Test Reference or Push Number')

    SCPT_DPTH = models.FloatField(primary_key=True, verbose_name='Depth of Result (m)')
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
    
'''==================================== LAB RESULTS ===================================='''

'''=================================== CLASSIFICATION ===================================='''

class LNMC(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='moisture_content', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location Identifier')
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
        return f"{self.SAMP_ID} - {self.LNMC_MC}% Moisture Content"

class GRAG(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='particle_size_distribution', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location Identifier')
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
    FILE_FSET = models.CharField(max_length=255, verbose_name='Associated File Reference')
    SPEC_BASE = models.FloatField(verbose_name='Depth to Base of Specimen (m)')
    GRAG_DEV = models.TextField(verbose_name='Deviation from the Specified Test Procedure')
    GRAG_PDEN = models.FloatField(verbose_name='Particle Density (Mg/m3)')
    GRAG_PRET = models.CharField(max_length=255, verbose_name='Method of Pre-treatment')
    GRAG_SUFF = models.CharField(max_length=2, verbose_name='Sufficiency of Soil Tested')
    GRAG_EXCL = models.TextField(verbose_name='Exclusion Remark')

    def __str__(self):
        return f"{self.SAMP_ID} - {self.GRAG_FINE}% fines"
    
class GRAT(models.Model):
    SAMP_ID = models.ForeignKey(GRAG, on_delete=models.CASCADE, related_name='particle_size_distribution_data', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location Identifier')
    SAMP_TOP = models.FloatField(verbose_name='Depth to Top of Sample (m)')
    SAMP_REF = models.CharField(max_length=50, verbose_name='Sample Reference')
    SAMP_TYPE = models.CharField(max_length=50, verbose_name='Sample Type')
    SPEC_REF = models.CharField(max_length=50, verbose_name='Specimen Reference')
    SPEC_DPTH = models.FloatField(verbose_name='Depth to Top of Test Specimen (m)', help_text="m")
    GRAT_SIZE = models.FloatField(verbose_name='Sieve or Particle Size (mm)', help_text="mm")
    GRAT_PERP = models.FloatField(verbose_name='Percentage Passing/Finer than GRAT_SIZE (%)', help_text="%")
    GRAT_TYPE = models.CharField(max_length=50, verbose_name='Test Type')
    GRAT_REM = models.TextField(verbose_name='Remarks')
    FILE_FSET = models.CharField(max_length=255, verbose_name='Associated File Reference')
    
    def __str__(self):
        return f"{self.SAMP_ID} - {self.GRAT_SIZE} mm - {self.GRAT_PERP} passing (%)"
    
class LDEN(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='bulk_density', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, verbose_name='Location Identifier')
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

class LLPL(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='atterberg', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location Identifier')
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

class LPDN(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='particle_density', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location Identifier')
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
    
class LRES(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='electrical_resistivity', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location Identifier')
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

class LTCH(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='thermal_conductivity', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location Identifier')
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
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='Associated File Reference')

    def __str__(self):
        return f"{self.SAMP_ID} - Conductivity: {self.LTCH_TCON} (W/(K-m)) Resistivity: {self.LTCH_TRES} (K-m/W)"
    
class RELD(models.Model):
    SAMP_ID = models.ForeignKey(SAMP, on_delete=models.CASCADE, related_name='minmax', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location Identifier')
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
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='Associated File Reference')
    SPEC_BASE = models.FloatField(null=True, verbose_name='Depth to Base of Specimen')
    RELD_DEV = models.TextField(blank=True, verbose_name='Deviation from the Specified Procedure')

    def __str__(self):
        return f"{self.SAMP_ID} - Min: {self.RELD_DMIN} Max: {self.RELD_DMAX}"
    
from django.db import models

class PTST(models.Model):
    SAMP_ID = models.ForeignKey('SAMP', on_delete=models.CASCADE, related_name='permeability', verbose_name='Sample ID')

    LOCA_ID = models.CharField(max_length=50, blank=True, verbose_name='Location Identifier')
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
    FILE_FSET = models.CharField(max_length=255, blank=True, verbose_name='Associated File Reference')
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
        return f"{self.SAMP_ID} - K: {self.PTST_K} m/x"
    
# Look at trying out Django Forms 
# from django import forms
# from .models import SAMP

# class SampForm(forms.ModelForm):
#     class Meta:
#         model = SAMP
#         fields = '__all__'
#         widgets = {
#             'SAMP_TOP': forms.NumberInput(attrs={'required': 'required'}),
#             'SAMP_REF': forms.TextInput(attrs={'required': 'required'}),
#             'SAMP_TYPE': forms.TextInput(attrs={'required': 'required'}),
#             'SAMP_ID': forms.TextInput(attrs={'required': 'required'}),
#         }