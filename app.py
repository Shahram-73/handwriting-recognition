import os
import config
import modules.getdata as getdata
from modules.preprocessing import ParagraphExtractor
from modules.preprocessing import Preprocessing
################ Step 1 of the pipeline: download the raw data  ################

# downloder = getdata.Downloader()
# downloder.download(config.google_ids.get('ascii') , 'ascii.zip').extract()
# downloder.download(config.google_ids.get('xml') , 'xml.zip').extract()
# downloder.download(config.google_ids.get('forms') , 'forms.zip').extract()


################ Step 2 of the pipeline" extract the paragraph   ################

# paragraph = ParagraphExtractor(offset=10)
# paragraph.extractAll(
#     config.path.get('forms'),
#     config.path.get('xml'),
# )

################ Step 3 of the pipeline" extract the paragraph   ################

# preprocessor = Preprocessing()
# preprocessor.apply_to_directory(
#     config.path.get('paragraphs')
# )