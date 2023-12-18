import zen

with open("./rule-engine-jdm-files//shipping-fees.json", "r") as f:
  content = f.read()

engine = zen.ZenEngine()

def zen_api(args):
  decision = engine.create_decision(content)
  result = decision.evaluate(args)
  return result
