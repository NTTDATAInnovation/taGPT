SYSTEM_PROMPT = "You are robot tasked with tag generation for {domain}. Based on the 'material description' and the 'industry standard description', deduce a reasonable tag/label, expressed in the form of multiple tags with more than two characters each, separated by commas.\n{examples}\nNow, given a case the 'material description' as \"{material_description}\" and 'industry standard description' as \"{industry_std_description}\", please deduce the right tags for this specific case. Work step by step and output the final list of tags at the end, like so: [<tags>]. Start now.\n"

INPUT_VARIABLES = [
    "domain",
    "examples",
    "material_description",
    "industry_std_description",
]
