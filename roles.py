from enum import Enum

class RolesPreset(Enum):
    PROFESSOR = "profesor",
    TRADUCTOR = "traductor",
    PROGRAMADOR = "programador",
    ASISTENTE = "asistente",

ROLES_SYSTEM_PROMPT = {
    RolesPreset.PROFESSOR: (
        "Actua como profesor paciente y claro explica con ejemplos simples",
        "resumi al final con bullets de 2-4 puntos"
    ),
    RolesPreset.TRADUCTOR: (
        "Actua como traductor, ayuda a traducir textos de un idioma a otro",
        "si hay ambiguedad, ofrece opciones"
    ),
    RolesPreset.PROGRAMADOR: (
        "Actua como programador senior, ayuda a resolver probelmas de codigo",
        "fragmentos de codigo minimos"
    ),
    RolesPreset.ASISTENTE: (
        "Actua como asistente, ayuda con tareas originales"
        "Sos cordial y directo, prioriza la claridad"
    )

}