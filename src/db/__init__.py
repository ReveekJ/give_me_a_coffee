from src.db.food_orders.models import *

from src.db.organizations.models import *
from src.db.organizations.schemas import *

from src.db.menu.models import *
from src.db.menu.schemas import *

from src.db.owners.models import *
from src.db.owners.schemas import *

from src.db.tasks.models import *
from src.db.tasks.schemas import *

from src.db.workers.models import *
from src.db.workers.schemas import *


OwnerSchema.model_rebuild()
OrganizationSchema.model_rebuild()
WorkerSchema.model_rebuild()
TaskSchema.model_rebuild()
FoodSchema.model_rebuild()
FoodGroupSchema.model_rebuild()
