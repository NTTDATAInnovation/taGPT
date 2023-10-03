# SYSTEM_PROMPT = "You are robot tasked with tag generation for {domain}. Based on the 'material description' and the 'industry standard description', deduce a reasonable tag/label, expressed in the form of a comma-seperated list, like so: [<tag 1>, ..., <tag n>].\n\n{examples}\nGiven a case with a 'material description' of \"{material_description}\" and an 'industry standard description' of \"{industry_std_description}\", please deduce the right tags for this case and return only the final list of tags.\n"  # TODO: Make dynamic

# INPUT_VARIABLES = [
#     "domain",
#     "examples",
#     "material_description",
#     "industry_std_description",
# ]  # TODO: Make dynamic


# SYSTEM_PROMPT = "You are a manufacturing expert and your task is to select a few tags for a given manufacturing description from the provided list of tags that relates more to the input.  Below is the given tags list surrounded by triple quotes:\n\n\"\"\"\n1: Electrical\n2: Ventilation\n3: 35W\n4: Battery\n5: Power\n6: Fastener\n7: Metal\n8: Engine\n9: Motor\n10: Hand-held\n11: Tool\n\"\"\"\n\nHere are a few example of the input and output surrounded by triple equals sign:\n\n===\nInput: \nMaterial description is \"WIRE END RED DZ5-CE 010\"\nOutput: \n[\"Electrical\"]\n\nInput: \nMaterial description is \"VENTILATOR 24VDC 35W Q=510M3/H 150T ECO\"\nOutput: \n[\"Ventilation\", \"35W\"]\n\nInput: \nMaterial description is \"BATTERI\"\nOutput: \n[\"Battery\", \"Power\"]\n\nInput: \nMaterial description is \"CLAMPING SCREW W. HANDLE FOR SOLD FIXTUR\"\nOutput:\n [\"Fastener\", \"Metal\"]\n===\n\nInput: \nMaterial description is \"{material_description}\"\nOutput: \n"


SYSTEM_PROMPT = """Infer a description and reasonable tags for industrial components. Take inspiration from the following examples:

Description: The "HYDRAULIC VALVE" is used to control the flow and direction of hydraulic fluid within a hydraulic system. It regulates the pressure, flow rate, and direction of hydraulic fluid to perform various functions such as actuating cylinders, controlling motors, and operating hydraulic machinery. Tags: [hydraulic, fluid, flow control, pressure].

Description: The "DRUM MOTOR Ø80X343MM 0.07KW" is used for conveyor belt systems. It belongs to the class of motorized drum systems or conveyor drive systems, which play a crucial role in the transportation of materials in various industries such as manufacturing, logistics, and warehousing. Tags: [belt, conveyor, drum roller, motorized system].

Description: The "SENSOR" is used to detect the presence or conditions in the environment. It is a critical component that regulates the operation of machines and systems across different industries. Tags: [sense, detection, movement, object].

{material_description}
"""

INPUT_VARIABLES = [
    "material_description"
]
