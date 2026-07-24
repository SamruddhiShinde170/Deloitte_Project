import json
import datetime

# Helper: convert ISO string → epoch milliseconds
def iso_to_epoch_ms(iso_str):
    dt = datetime.datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

# Convert Format 1 → unified format
def convertFromFormat1(jsonObject):
    return {
        "id": jsonObject["deviceId"],
        "timestamp": iso_to_epoch_ms(jsonObject["time"]),
        "temperature": jsonObject["metrics"]["temperature"]
    }


# Convert Format 2 → unified format
def convertFromFormat2(jsonObject):
    return {
        "id": jsonObject["id"],
        "timestamp": int(jsonObject["time"]) * 1000,  # seconds → ms
        "temperature": jsonObject["readings"]["temperature"]
    }

# ------------------------------
# Test runner
# ------------------------------
if __name__ == "__main__":
    # Load input files
    with open("data-1.json") as f1:
        data1 = json.load(f1)
    with open("data-2.json") as f2:
        data2 = json.load(f2)
    with open("data-result.json") as fr:
        expected = json.load(fr)

    # Run conversions
    result1 = convertFromFormat1(data1)
    result2 = convertFromFormat2(data2)

    # Tests
    assert result1 == expected, f"Format1 conversion failed: {result1} != {expected}"
    assert result2 == expected, f"Format2 conversion failed: {result2} != {expected}"

    print("All tests passed ✅")
