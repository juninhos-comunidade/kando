"""Serializers do app jobs."""
# serializers.py
from rest_framework import serializers

from .models import JobPosting

MIN_RAW_TEXT_LENGTH = 150


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = [
            "id",
            "submitted_by",
            "source",
            "raw_text",
            "file_url",
            "extracted_text",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "submitted_by",
            "file_url",
            "extracted_text",
            "created_at",
        ]

    def validate(self, data):
        source = data.get("source")
        raw_text = data.get("raw_text")

        if source == JobPosting.Source.TEXT:
            if not raw_text or not raw_text.strip():
                raise serializers.ValidationError(
                    {"raw_text": "O campo raw_text não pode estar vazio quando source='text'."}
                )

            cleaned = raw_text.strip()
            if len(cleaned) < MIN_RAW_TEXT_LENGTH:
                raise serializers.ValidationError(
                    {
                        "raw_text": (
                            f"A descrição da vaga deve ter no mínimo "
                            f"{MIN_RAW_TEXT_LENGTH} caracteres (atual: {len(cleaned)})."
                        )
                    }
                )
            data["raw_text"] = cleaned

        return data

    def create(self, validated_data):
        validated_data["submitted_by"] = self.context["request"].user
        return super().create(validated_data)