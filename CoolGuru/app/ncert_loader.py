import json
import os

  DATA_PATH = "data"

  def load_subject_data(subject):
      filename = f"class6_{subject.lower()}.json"
      path = os.path.join(DATA_PATH, filename)

      if not os.path.exists(path):
          return None

      with open(path, "r", encoding="utf-8") as f:
          return json.load(f)

  # Example usage:
  if __name__ == "__main__":
      data = load_subject_data("science")
      print(data)

