#!/usr/bin/env python3
"""
Amr Torky Institute — Cryptographic SHA-256 Digital Certificate Generator
Generates tamper-proof accreditation digests under ISO/IEC 17025 standards.
Author: Scientist Amr Torky
"""
import time
import hashlib
import json
import sys

def issue_certificate(student_name, track_id, exam_score):
    if exam_score < 80.0:
        print(f"❌ Accreditation Failed: Score {exam_score:.1f}% is below mandatory 80.0% threshold.")
        sys.exit(1)

    cert_data = {
        "institution": "Amr Torky Institute for Advanced Physical Engineering",
        "chief_architect": "Scientist Amr Torky",
        "student_name": student_name,
        "track_id": track_id,
        "exam_score_percent": exam_score,
        "tuition_standard_usd": 12000.0,
        "tuition_paid_net_usd": 6000.0,
        "issue_timestamp": int(time.time()),
        "accreditation_status": "VERIFIED & CERTIFIED",
        "verification_protocol": "SHA-256 Cryptographic Release Digest",
        "iso_standard": "ISO/IEC 17025:2017"
    }

    raw_bytes = json.dumps(cert_data, sort_keys=True).encode('utf-8')
    digest = hashlib.sha256(raw_bytes).hexdigest()
    cert_data["sha256_digest"] = digest

    filename = f"CERTIFICATE_{student_name.replace(' ', '_').upper()}.json"
    with open(filename, "w") as f:
        json.dump(cert_data, f, indent=2)

    print(f"✓ Certificate Issued Successfully by Scientist Amr Torky!")
    print(f"   Graduate: {student_name}")
    print(f"   Track: {track_id}")
    print(f"   SHA-256 Digest: {digest}")
    return digest

if __name__ == "__main__":
    if len(sys.argv) > 3:
        issue_certificate(sys.argv[1], sys.argv[2], float(sys.argv[3]))
    else:
        issue_certificate("Dr. Sarah Jenkins", "CMSP-Track-01", 92.5)
