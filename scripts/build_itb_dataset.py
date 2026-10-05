"""
Dataset generation engine for Institut Teknologi Bandung (ITB) Study Programs Directory.
Generates comprehensive prodi catalog across S1 and Pascasarjana (S2/S3) with TPB faculties,
multi-campus distribution (Ganesa, Jatinangor, Cirebon), international accreditations
(ABET, ASIIN, AACSB, KAAB, RSC), quotas (SNBP, SNBT, SM-ITB), curriculum, and career pathways.
Zero emoji compliance strictly enforced.
"""

import json
import csv
import os
import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(ROOT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

ITB_METADATA = {
    "universitas": "Institut Teknologi Bandung",
    "universitas_en": "Bandung Institute of Technology",
    "singkatan": "ITB",
    "motto": "In Harmonia Progressio",
    "tahun_berdiri": 1920,
    "rektor": "Prof. Reini Wirahadikusumah, Ph.D.",
    "website_utama": "https://www.itb.ac.id",
    "portal_spmb": "https://admission.itb.ac.id",
    "kampus": [
        {
            "id": "ganesa",
            "nama": "Kampus ITB Ganesa",
            "lokasi": "Kota Bandung, Jawa Barat",
            "deskripsi": "Kampus utama bersejarah ITB, pusat fakultas teknik inti, sains murni, arsitektur, dan seni rupa."
        },
        {
            "id": "jatinangor",
            "nama": "Kampus ITB Jatinangor",
            "lokasi": "Kabupaten Sumedang, Jawa Barat",
            "deskripsi": "Kampus modern pengembangan rekayasa hayati, pertanian terapan, kehutanan, infrastruktur lingkungan, dan SBM."
        },
        {
            "id": "cirebon",
            "nama": "Kampus ITB Cirebon",
            "lokasi": "Kabupaten Cirebon, Jawa Barat",
            "deskripsi": "Kampus pengembangan strategis daerah untuk teknik industri, perminyakan, pertambangan, dan kriya seni."
        }
    ],
    "jalur_masuk": [
        "SNBP (Seleksi Nasional Berdasarkan Prestasi)",
        "SNBT (Seleksi Nasional Berdasarkan Tes / UTBK)",
        "Seleksi Mandiri ITB (SM-ITB Ujian Mandiri & Portofolio)",
        "International Undergraduate Program (IUP ITB)"
    ],
    "akreditasi_internasional_list": ["ABET", "ASIIN", "AACSB", "KAAB", "RSC", "IABEE"]
}

RAW_PRODI = [
    # =========================================================================
    # 1. STEI - Sekolah Teknik Elektro dan Informatika (Ganesa)
    # =========================================================================
    {
        "id": "s1-teknik-informatika",
        "kode": "13501",
        "nama": "Teknik Informatika",
        "nama_en": "Informatics / Computer Science",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "STEI-K (Komputasi)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Teknik Elektro dan Informatika", "fakultas_singkatan": "STEI",
        "akreditasi": "Unggul", "akreditasi_skor": "385",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 120, "dt_snbp": 36, "dt_snbt": 48, "dt_smitb": 36,
        "website": "https://stei.itb.ac.id/if",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Program studi ilmu komputasi paling prestisius di Indonesia, berfokus pada rekayasa perangkat lunak skala masif, algoritma lanjutan, kecerdasan buatan, dan komputasi awan.",
            "en": "Indonesia's apex computer science degree emphasizing massive-scale software engineering, advanced algorithms, AI, and cloud architectures."
        },
        "fokus": {
            "id": ["Kompleksitas Algoritma & Teori Komputasi", "Rekayasa Perangkat Lunak Skala Besar", "Kecerdasan Artifisial & Pembelajaran Mesin", "Sistem Terdistribusi & Komputasi Awan"],
            "en": ["Algorithmic Complexity & Computation Theory", "Large-Scale Software Engineering", "Artificial Intelligence & Machine Learning", "Distributed Cloud Computing Architectures"]
        },
        "karir": {
            "id": ["Staff / Lead Software Engineer di Global Big Tech", "AI / Machine Learning Research Engineer", "System Architect & Cloud Infrastructure Lead", "Tech Founder / Chief Technology Officer (CTO)"],
            "en": ["Global Big Tech Staff Software Engineer", "AI / Machine Learning Engineer", "System Architect & Cloud Lead", "Technology Founder / CTO"]
        }
    },
    {
        "id": "s1-sistem-dan-teknologi-informasi",
        "kode": "18201",
        "nama": "Sistem dan Teknologi Informasi",
        "nama_en": "Information System and Technology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "STEI-K (Komputasi)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Teknik Elektro dan Informatika", "fakultas_singkatan": "STEI",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 90, "dt_snbp": 27, "dt_snbt": 36, "dt_smitb": 27,
        "website": "https://stei.itb.ac.id/sti",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Sinergi rekayasa teknologi informasi dan tata kelola enterprise, mencakup arsitektur sistem informasi perbankan/e-commerce, keamanan siber, dan rekayasa data.",
            "en": "Synergy of IT engineering and enterprise governance, encompassing financial/e-commerce system architecture, cybersecurity, and data engineering."
        },
        "fokus": {
            "id": ["Arsitektur Enterprise & Tata Kelola SI", "Keamanan Siber & Kriptografi Terapan", "Rekayasa Data & Analitika Bisnis", "Manajemen Proyek Teknologi Informasi"],
            "en": ["Enterprise IT Architecture & Governance", "Applied Cybersecurity & Threat Defense", "Data Engineering & Analytics", "Digital Product & IT Project Management"]
        },
        "karir": {
            "id": ["Enterprise Solutions Architect", "Cybersecurity Specialist & Penetration Tester", "Data Engineer & Pipeline Lead", "Digital Product Manager"],
            "en": ["Enterprise Solutions Architect", "Cybersecurity Lead Specialist", "Data Infrastructure Engineer", "Digital Product Manager"]
        }
    },
    {
        "id": "s1-teknik-elektro",
        "kode": "13201",
        "nama": "Teknik Elektro",
        "nama_en": "Electrical Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "STEI-R (Rekayasa)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Teknik Elektro dan Informatika", "fakultas_singkatan": "STEI",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 110, "dt_snbp": 33, "dt_snbt": 44, "dt_smitb": 33,
        "website": "https://stei.itb.ac.id/el",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Pendidikan teknik elektro tertua di Indonesia, terakreditasi ABET, berfokus pada mikroelektronika semikonduktor, pemrosesan sinyal, sistem kendali, dan instrumentasi cerdas.",
            "en": "Oldest ABET-accredited electrical engineering in Indonesia focusing on semiconductor microelectronics, signal processing, and intelligent control systems."
        },
        "fokus": {
            "id": ["Mikroelektronika & Perancangan IC / VLSI", "Sistem Kendali Otomasi & Robotika", "Pengolahan Sinyal Digital & Telekomunikasi", "Elektronika Daya & Sensor Biomedis"],
            "en": ["Microelectronics & IC/VLSI Chip Design", "Control Systems Automation & Robotics", "Digital Signal Processing & Telecom", "Power Electronics & Smart Sensors"]
        },
        "karir": {
            "id": ["Semiconductor / IC Design Engineer", "Automation & Control Systems Engineer", "Hardware Systems Design Specialist", "Robotics & Firmware Engineer"],
            "en": ["Semiconductor / IC Chip Designer", "Industrial Automation Engineer", "Embedded Hardware Designer", "Robotics Firmware Engineer"]
        }
    },
    {
        "id": "s1-teknik-tenaga-listrik",
        "kode": "18001",
        "nama": "Teknik Tenaga Listrik",
        "nama_en": "Power Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "STEI-R (Rekayasa)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Teknik Elektro dan Informatika", "fakultas_singkatan": "STEI",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 32, "dt_smitb": 24,
        "website": "https://stei.itb.ac.id/ep",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Pusat unggulan rekayasa transmisi daya tegangan tinggi, pembangkit energi terbarukan (surya, hidro, bayu), dan jaringan listrik pintar (smart grid).",
            "en": "Center of excellence for high-voltage power transmission, renewable energy generation (solar, hydro, wind), and resilient smart grid systems."
        },
        "fokus": {
            "id": ["Sistem Pembangkit & Transmisi Daya Listrik", "Jaringan Listrik Pintar (Smart Grid)", "Konversi Energi Terbarukan & Penyimpanan Baterai", "Proteksi Tegangan Tinggi & Gardu Induk"],
            "en": ["Power Generation & High-Voltage Transmission", "Smart Grid Infrastructure", "Renewable Energy Conversion & Battery Storage", "High-Voltage Protection & Substation Design"]
        },
        "karir": {
            "id": ["Power Systems Engineer (PT PLN / Pembangkit)", "Smart Grid & Renewable Energy Consultant", "High-Voltage Protection Specialist", "Electrical Substation Project Lead"],
            "en": ["Power Systems Grid Engineer", "Renewable Energy Project Consultant", "High-Voltage Protection Engineer", "Substation Commissioning Specialist"]
        }
    },
    {
        "id": "s1-teknik-telekomunikasi",
        "kode": "18101",
        "nama": "Teknik Telekomunikasi",
        "nama_en": "Telecommunication Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "STEI-R (Rekayasa)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Teknik Elektro dan Informatika", "fakultas_singkatan": "STEI",
        "akreditasi": "Unggul", "akreditasi_skor": "381",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 32, "dt_smitb": 24,
        "website": "https://stei.itb.ac.id/et",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Mempelajari jaringan seluler nirkabel 5G/6G, komunikasi satelit, antena gelombang mikro, transmisi serat optik pita lebar, dan rekayasa protokol internet.",
            "en": "Focuses on 5G/6G wireless networks, satellite communications, microwave antenna engineering, fiber optic photonics, and internet protocols."
        },
        "fokus": {
            "id": ["Jaringan Nirkabel 5G/6G & Seluler", "Rekayasa Antena Gelombang Mikro & Radar", "Komunikasi Satelit & Optik", "Protokol Jaringan & Keamanan Komunikasi"],
            "en": ["5G/6G Wireless Cellular Networks", "RF Antenna & Radar Engineering", "Satellite & Fiber Optic Telecommunications", "Network Protocol Architecture"]
        },
        "karir": {
            "id": ["Telecommunication RF / Core Network Engineer", "Satellite & Microwave Communications Specialist", "Network Operations Lead di Telco Global", "Optical Fiber Transmission Specialist"],
            "en": ["Telecom Core / RF Network Engineer", "Satellite Communications Lead", "Telco Operations Director", "Photonics & Optical Transmission Specialist"]
        }
    },
    {
        "id": "s1-teknik-biomedis",
        "kode": "18301",
        "nama": "Teknik Biomedis",
        "nama_en": "Biomedical Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "STEI-R (Rekayasa)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Teknik Elektro dan Informatika", "fakultas_singkatan": "STEI",
        "akreditasi": "Unggul", "akreditasi_skor": "378",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 24, "dt_smitb": 18,
        "website": "https://stei.itb.ac.id/eb",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Perancangan teknologi instrumentasi medis mutakhir, sensor pemantau kesehatan, pengolahan sinyal EEG/ECG, dan kecerdasan diagnostik komputer.",
            "en": "Engineering of advanced diagnostic medical instrumentation, physiological biosensors, EEG/ECG biosignal processing, and healthcare AI."
        },
        "fokus": {
            "id": ["Instrumentasi Alat Medis & Sensor Tubuh", "Pemrosesan Sinyal Fisiologis & Citra Medis", "Informatika Medis & AI Diagnostik", "Biomekanika & Alat Bantu Rehabilitasi"],
            "en": ["Clinical Medical Instrumentation & Biosensors", "Physiological Signal & Image Processing", "Medical Informatics & Diagnostic AI", "Biomechanics & Rehabilitation Engineering"]
        },
        "karir": {
            "id": ["Biomedical Device R&D Specialist", "Clinical Systems Engineer Rumah Sakit", "Diagnostic Equipment Product Specialist", "Healthcare AI Solutions Developer"],
            "en": ["Biomedical Device R&D Engineer", "Clinical Systems Hospital Engineer", "Diagnostic Medical Specialist", "Healthcare AI Solutions Developer"]
        }
    },

    # =========================================================================
    # 2. FTI - Fakultas Teknologi Industri (Ganesa & Jatinangor)
    # =========================================================================
    {
        "id": "s1-teknik-kimia",
        "kode": "13001",
        "nama": "Teknik Kimia",
        "nama_en": "Chemical Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTI-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknologi Industri", "fakultas_singkatan": "FTI",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 120, "dt_snbp": 36, "dt_snbt": 48, "dt_smitb": 36,
        "website": "https://che.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Teknik kimia peringkat tertinggi di Indonesia, terakreditasi ABET, berfokus pada desain pabrik petrokimia, termodinamika terapan, proses katalitik, dan bioenergi.",
            "en": "Premier ABET-accredited chemical engineering department in Indonesia, specializing in petrochemical plant design, thermodynamics, catalysis, and clean bioenergy."
        },
        "fokus": {
            "id": ["Perancangan Pabrik Kimia & Simulasi Aspen", "Termodinamika Rekayasa & Fenomena Perpindahan", "Teknologi Katalisis & Petrokimia", "Transisi Energi Hijau & Hidrogen"],
            "en": ["Chemical Plant Simulation & Aspen Hysys", "Thermodynamics & Transport Phenomena", "Catalysis & Petrochemical Engineering", "Green Hydrogen & Energy Transition"]
        },
        "karir": {
            "id": ["Process Engineer Migas & Petrokimia Multinasional", "Plant Commissioning & Operations Lead", "Clean Energy & Hydrogen Process Specialist", "Process Safety & Hazard Engineer"],
            "en": ["Chemical Process Engineer (Oil & Gas)", "Plant Commissioning Operations Lead", "Hydrogen & Clean Fuel Specialist", "Industrial Process Safety Lead"]
        }
    },
    {
        "id": "s1-teknik-industri",
        "kode": "13401",
        "nama": "Teknik Industri",
        "nama_en": "Industrial Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTI-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknologi Industri", "fakultas_singkatan": "FTI",
        "akreditasi": "Unggul", "akreditasi_skor": "385",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 130, "dt_snbp": 39, "dt_snbt": 52, "dt_smitb": 39,
        "website": "https://ti.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Pelopor teknik industri di Indonesia, mengintegrasikan riset operasi, ergonomi sistem terpadu, manajemen rantai pasok global, dan analitika keputusan manufaktur.",
            "en": "Pioneering industrial engineering department integrating operations research, ergonomics, global supply chains, and enterprise manufacturing analytics."
        },
        "fokus": {
            "id": ["Riset Operasi & Optimasi Sistem Stokastik", "Manajemen Rantai Pasok Global (SCM)", "Ergonomi & Rekayasa Faktor Manusia", "Sistem Kualitas Terpadu & Lean Six Sigma"],
            "en": ["Operations Research & Stochastic Optimization", "Global Supply Chain Network Logistics", "Cognitive Ergonomics & Systems Safety", "Total Quality & Lean Six Sigma"]
        },
        "karir": {
            "id": ["Supply Chain Director Korporasi Global", "Management & Strategy Consultant (MBB / Big 4)", "Product / Operations Program Manager", "Manufacturing Continuous Improvement Lead"],
            "en": ["Global Supply Chain Director", "Strategy Management Consultant", "Product Operations Lead", "Industrial Operations Director"]
        }
    },
    {
        "id": "s1-manajemen-rekayasa-industri",
        "kode": "14401",
        "nama": "Manajemen Rekayasa Industri",
        "nama_en": "Engineering Management",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTI-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknologi Industri", "fakultas_singkatan": "FTI",
        "akreditasi": "Unggul", "akreditasi_skor": "381",
        "akreditasi_internasional": ["ABET"],
        "daya_tampung": 75, "dt_snbp": 22, "dt_snbt": 30, "dt_smitb": 23,
        "website": "https://mri.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Menjembatani keahlian rekayasa teknik dan kepemimpinan bisnis manajemen, berfokus pada inovasi produk teknologi, komersialisasi riset, dan analisis kelayakan proyek.",
            "en": "Bridges engineering problem-solving with business leadership, focusing on technology innovation, research commercialization, and capital project feasibility."
        },
        "fokus": {
            "id": ["Manajemen Proyek Rekayasa Skala Besar", "Inovasi & Pengembangan Produk Baru (NPD)", "Ekonomi Teknik & Analisis Kelayakan Investasi", "Komersialisasi Teknologi & Venture"],
            "en": ["Capital Project Engineering Management", "New Product Development (NPD)", "Engineering Economics & Financial Feasibility", "Technology Commercialization & Venturing"]
        },
        "karir": {
            "id": ["Technical Project Manager Megaproyek", "Product Manager Teknologi & Manufaktur", "Technology Commercialization Lead", "Business Process Architect"],
            "en": ["Engineering Project Director", "Tech Hardware Product Manager", "Technology Commercialization Lead", "Enterprise Process Architect"]
        }
    },
    {
        "id": "s1-teknik-fisika",
        "kode": "13301",
        "nama": "Teknik Fisika",
        "nama_en": "Engineering Physics",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTI-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknologi Industri", "fakultas_singkatan": "FTI",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 100, "dt_snbp": 30, "dt_snbt": 40, "dt_smitb": 30,
        "website": "https://tf.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Pendidikan rekayasa interdisipliner menguasai instrumentasi industri modern, fisika bangunan & akustik, fotonika, dan sistem otomasi kendali cerdas.",
            "en": "Interdisciplinary engineering mastering industrial instrumentation, building acoustics, photonics, and intelligent control automation."
        },
        "fokus": {
            "id": ["Instrumentasi Industri & Sistem Kendali Terdistribusi (DCS)", "Fisika Bangunan, Tata Suara, & Akustik Ruang", "Teknologi Fotonika & Sensor Optik", "Efisiensi Energi & Manajemen Fasilitas"],
            "en": ["Industrial Instrumentation & Distributed Controls", "Building Physics & Architectural Acoustics", "Photonics & Optical Fiber Sensors", "Building Energy Management & Audit"]
        },
        "karir": {
            "id": ["Instrumentation & Control Engineer Migas", "Acoustics & Lighting Consultant", "Building Energy Efficiency Specialist", "Photonics & Sensors R&D Engineer"],
            "en": ["Instrumentation & Control Engineer", "Architectural Acoustic Consultant", "Energy Auditor & Facility Engineer", "Photonics Sensor R&D Specialist"]
        }
    },
    {
        "id": "s1-teknik-pangan",
        "kode": "14301",
        "nama": "Teknik Pangan",
        "nama_en": "Food Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTI-Jatinangor",
        "lokasi": "Kampus ITB Jatinangor (Sumedang)",
        "fakultas": "Fakultas Teknologi Industri", "fakultas_singkatan": "FTI",
        "akreditasi": "Unggul", "akreditasi_skor": "375",
        "akreditasi_internasional": [],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 24, "dt_smitb": 18,
        "website": "https://fti.itb.ac.id/pangan",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Menerapkan prinsip teknik kimia dan proses fisik pada industri pangan skala massal, teknologi pengawetan non-termal, dan formulasi pangan fungsional.",
            "en": "Applies chemical engineering and transport phenomena to large-scale food manufacturing, non-thermal preservation, and functional food formulation."
        },
        "fokus": {
            "id": ["Rekayasa Proses Termal & Pengawetan Pangan", "Desain Pabrik Pengolahan Pangan Skala Industri", "Reologi Pangan & Karakterisasi Sensori", "Keamanan Pangan & Sistem HACCP"],
            "en": ["Thermal Food Processing Engineering", "Industrial Food Processing Plant Design", "Food Rheology & Sensory Mechanics", "HACCP & Food Quality Engineering"]
        },
        "karir": {
            "id": ["Food Process Engineer di FMCG Pangan", "R&D Formulation Scientist Industri Makanan", "Food Quality Assurance (QA) Director", "Packaging & Preservation Engineer"],
            "en": ["Food Process Plant Engineer", "Food Formulation R&D Scientist", "Quality Assurance (HACCP) Manager", "Food Packaging Engineer"]
        }
    },
    {
        "id": "s1-teknik-bioenergi-kemurgi",
        "kode": "14501",
        "nama": "Teknik Bioenergi dan Kemurgi",
        "nama_en": "Bioenergy and Chemurgy Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTI-Jatinangor",
        "lokasi": "Kampus ITB Jatinangor (Sumedang)",
        "fakultas": "Fakultas Teknologi Industri", "fakultas_singkatan": "FTI",
        "akreditasi": "Unggul", "akreditasi_skor": "376",
        "akreditasi_internasional": [],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 24, "dt_smitb": 18,
        "website": "https://fti.itb.ac.id/bioenergi",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Konversi komoditas hayati non-pangan (sawit, biomassa, alga) menjadi bahan bakar nabati (biodiesel, bioavtur, biopellet) dan bahan kimia industri.",
            "en": "Converts non-food biological feedstocks into renewable biofuels (biodiesel, sustainable aviation fuel) and specialty bio-based industrial chemicals."
        },
        "fokus": {
            "id": ["Teknologi Kilang Nabati (Biorefinery)", "Sintesis Biodiesel & Sustainable Aviation Fuel (SAF)", "Kimia Polimer Hayati (Bioplastik)", "Termokimia Biomassa (Gasifikasi & Pirolisis)"],
            "en": ["Biorefinery Processing Technologies", "SAF Biofuel Synthesis", "Biopolymers & Green Chemistry", "Biomass Thermochemical Conversion"]
        },
        "karir": {
            "id": ["Biorefinery Process Engineer", "Biofuels & Bioaviation Specialist", "Green Chemical Production Lead", "Renewable Energy Sustainability Analyst"],
            "en": ["Biorefinery Operations Engineer", "Biofuels Development Specialist", "Green Chemurgy Process Lead", "Renewable Energy Carbon Analyst"]
        }
    },

    # =========================================================================
    # 3. FTMD - Fakultas Teknik Mesin dan Dirgantara (Ganesa)
    # =========================================================================
    {
        "id": "s1-teknik-mesin",
        "kode": "13101",
        "nama": "Teknik Mesin",
        "nama_en": "Mechanical Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTMD",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknik Mesin dan Dirgantara", "fakultas_singkatan": "FTMD",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 120, "dt_snbp": 36, "dt_snbt": 48, "dt_smitb": 36,
        "website": "https://ftmd.itb.ac.id/mesin",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Pendidikan teknik mesin terkemuka dengan keunggulan termofluida, perancangan mekanik presisi, manufaktur otomasi, dan sistem penggerak kendaraan listrik.",
            "en": "Top mechanical engineering department advancing thermofluid dynamics, precision mechanical design, automation, and electric vehicle powertrain systems."
        },
        "fokus": {
            "id": ["Termodinamika Rekayasa & Dinamika Fluida", "Perancangan Mekanikal CAD/CAM/CAE", "Mekatronika, Robotika, & Sistem Kendali", "Teknologi Kendaraan Listrik (EV Powertrain)"],
            "en": ["Engineering Thermodynamics & CFD", "Precision Mechanical Design (CAD/CAE)", "Mechatronics & Robotics Automation", "Electric Vehicle Powertrain Dynamics"]
        },
        "karir": {
            "id": ["Mechanical Design & Simulation Engineer", "Pembangkitan & Power Plant Lead", "Automotive & EV Powertrain Specialist", "Maintenance & Reliability Director"],
            "en": ["Mechanical Design Engineer", "Power Generation Lead Engineer", "Automotive & EV Systems Engineer", "Reliability Maintenance Director"]
        }
    },
    {
        "id": "s1-teknik-dirgantara",
        "kode": "13601",
        "nama": "Teknik Dirgantara",
        "nama_en": "Aerospace / Aeronautical Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTMD",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknik Mesin dan Dirgantara", "fakultas_singkatan": "FTMD",
        "akreditasi": "Unggul", "akreditasi_skor": "383",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 75, "dt_snbp": 22, "dt_snbt": 30, "dt_smitb": 23,
        "website": "https://ftmd.itb.ac.id/dirgantara",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Satu-satunya program studi teknik kedirgantaraan tertua di Indonesia, mendidik perancang pesawat terbang, aerodinamika supersonik, avionika, dan wahana antariksa/drone.",
            "en": "Indonesia's premier aerospace engineering department training aircraft designers, supersonic aerodynamics experts, avionics engineers, and UAV/spacecraft architects."
        },
        "fokus": {
            "id": ["Aerodinamika & Dinamika Terbang Pesawat", "Struktur Ringan & Material Komposit Dirgantara", "Sistem Propulsi Jet & Roket", "Avionika & Sistem Kendali Wahana Terbang (UAV)"],
            "en": ["Aerodynamics & Aircraft Flight Mechanics", "Aerospace Lightweight Structures & Composites", "Jet Engine & Rocket Propulsion", "Avionics & Unmanned Aerial Systems (UAS)"]
        },
        "karir": {
            "id": ["Aircraft Design Engineer (PTDI / Airbus / Boeing)", "Avionics & Drone Systems Specialist", "Fleet Airline Technical Services Engineer", "Rocket & Propulsion Specialist di BRIN / LAPAN"],
            "en": ["Aerospace Design Engineer", "Avionics & Autonomous UAV Specialist", "Airline Technical Operations Lead", "Space Propulsion Research Scientist"]
        }
    },
    {
        "id": "s1-teknik-material",
        "kode": "13701",
        "nama": "Teknik Material",
        "nama_en": "Materials Science and Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTMD",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknik Mesin dan Dirgantara", "fakultas_singkatan": "FTMD",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 75, "dt_snbp": 22, "dt_snbt": 30, "dt_smitb": 23,
        "website": "https://ftmd.itb.ac.id/material",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Sintesis dan karakterisasi material maju, paduan logam superalloy, material baterai kendaraan listrik, polimer fungsional, dan analisis kegagalan komponen (failure analysis).",
            "en": "Advanced materials synthesis and characterization, superalloys, battery energy storage materials, polymers, and structural failure analysis."
        },
        "fokus": {
            "id": ["Karakterisasi Mikrostruktur & Difraksi Sinar-X", "Material Elektrokimia Sel Baterai EV", "Polimer Fungsional & Material Komposit", "Analisis Kegagalan & Uji Tak Merusak (NDT)"],
            "en": ["Microstructural Characterization (XRD/SEM)", "Battery Cell Materials & Solid Electrolytes", "Functional Polymers & Advanced Composites", "Failure Analysis & Non-Destructive Testing"]
        },
        "karir": {
            "id": ["Materials Engineer Industri Otomotif / Migas", "Battery Cell Materials R&D Lead", "Non-Destructive Testing (NDT) Specialist", "Metallurgical Failure Investigator"],
            "en": ["Materials & Corrosion Engineer", "EV Battery Cell Materials Scientist", "NDT Level-III Specialist", "Structural Failure Analyst"]
        }
    },

    # =========================================================================
    # 4. FTTM - Fakultas Teknik Pertambangan dan Perminyakan (Ganesa & Cirebon)
    # =========================================================================
    {
        "id": "s1-teknik-pertambangan",
        "kode": "12101",
        "nama": "Teknik Pertambangan",
        "nama_en": "Mining Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTTM-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknik Pertambangan dan Perminyakan", "fakultas_singkatan": "FTTM",
        "akreditasi": "Unggul", "akreditasi_skor": "383",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 110, "dt_snbp": 33, "dt_snbt": 44, "dt_smitb": 33,
        "website": "https://fttm.itb.ac.id/tambang",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Pendidikan pertambangan terdepan di Asia Tenggara, mencakup perencanaan tambang terbuka dan bawah tanah, geoteknik lereng tambang, peledakan batuan, dan reklamasi lingkungan.",
            "en": "Southeast Asia's premier mining engineering school, specializing in open-pit and underground mine planning, rock mechanics, blasting, and reclamation."
        },
        "fokus": {
            "id": ["Perencanaan & Desain Tambang Terbuka / Bawah Tanah", "Mekanika Batuan & Kestabilan Lereng", "Teknik Peledakan & Ventilasi Tambang", "Valuasi Cadangan Mineral & Reklamasi"],
            "en": ["Mine Design & Optimization (Whittle/Vulcan)", "Rock Mechanics & Slope Stability", "Rock Blasting & Underground Ventilation", "Mineral Reserve Valuation & Reclamation"]
        },
        "karir": {
            "id": ["Mine Planning Engineer di Perusahaan Tambang Global", "Rock Mechanics & Geotechnical Engineer", "Drill and Blast Specialist", "Mine Operations Superintendent"],
            "en": ["Mine Planning Engineer", "Rock Mechanics / Geotech Lead", "Drill & Blast Technical Specialist", "Mine Operations Superintendent"]
        }
    },
    {
        "id": "s1-teknik-perminyakan",
        "kode": "12201",
        "nama": "Teknik Perminyakan",
        "nama_en": "Petroleum Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTTM-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknik Pertambangan dan Perminyakan", "fakultas_singkatan": "FTTM",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 100, "dt_snbp": 30, "dt_snbt": 40, "dt_smitb": 30,
        "website": "https://tm.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Mempelajari teknik reservoir fluida hidrokarbon, pengeboran lepas pantai (offshore drilling), peningkatan perolehan minyak (EOR), dan penangkapan karbon bawah tanah (CCUS).",
            "en": "Hydrocarbon reservoir engineering, offshore well drilling, Enhanced Oil Recovery (EOR), and geological carbon sequestration (CCUS)."
        },
        "fokus": {
            "id": ["Teknik Reservoir & Simulasi Aliran Fluida", "Teknik Pengeboran (Drilling) Lepas Pantai", "Teknik Produksi & Artificial Lift", "Enhanced Oil Recovery (EOR) & CCUS"],
            "en": ["Reservoir Engineering & Dynamic Simulation", "Offshore Well Drilling Engineering", "Production Engineering & Well Stimulation", "Enhanced Oil Recovery & Carbon Sequestration"]
        },
        "karir": {
            "id": ["Reservoir Engineer di Korporasi Migas Multinasional", "Drilling Engineer Lepas Pantai", "Production & Well Completion Engineer", "Geothermal & CCUS Subsurface Engineer"],
            "en": ["Reservoir Engineer (Global Energy Majors)", "Offshore Drilling Engineer", "Production Operations Engineer", "Geothermal / CCUS Subsurface Lead"]
        }
    },
    {
        "id": "s1-teknik-geofisika",
        "kode": "12301",
        "nama": "Teknik Geofisika",
        "nama_en": "Geophysical Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTTM-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknik Pertambangan dan Perminyakan", "fakultas_singkatan": "FTTM",
        "akreditasi": "Unggul", "akreditasi_skor": "381",
        "akreditasi_internasional": ["ABET", "ASIIN"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 32, "dt_smitb": 24,
        "website": "https://tg.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Eksplorasi bawah permukaan bumi menggunakan metode seismik refleksi, elektromagnetik, gayaberat, dan magnetik untuk energi minyak, panas bumi, dan mitigasi bencana gempa.",
            "en": "Subsurface exploration utilizing reflection seismology, electromagnetics, and gravity to locate oil, geothermal energy, and evaluate earthquake hazards."
        },
        "fokus": {
            "id": ["Seismik Refleksi & Pemrosesan Sinyal Gelombang", "Eksplorasi Energi Panas Bumi (Geotermal)", "Metode Elektromagnetik & Geolistrik", "Inversi Geofisika & Pemodelan Subpermukaan"],
            "en": ["Reflection Seismic Processing & Imaging", "Geothermal Reservoir Geophysical Surveys", "Electromagnetic & Resistivity Surveys", "Geophysical Inversion & Subsurface Imaging"]
        },
        "karir": {
            "id": ["Exploration Geophysicist (Migas / Geotermal)", "Seismic Data Processing Specialist", "Geotechnical Site Investigation Lead", "Seismologist Peneliti Bencana Kebumian"],
            "en": ["Energy Exploration Geophysicist", "Seismic Data Processing Lead", "Geotechnical Geophysical Surveyor", "Geohazard Seismological Analyst"]
        }
    },
    {
        "id": "s1-teknik-metalurgi",
        "kode": "12501",
        "nama": "Teknik Metalurgi",
        "nama_en": "Metallurgical Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTTM-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknik Pertambangan dan Perminyakan", "fakultas_singkatan": "FTTM",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 90, "dt_snbp": 27, "dt_snbt": 36, "dt_smitb": 27,
        "website": "https://fttm.itb.ac.id/metalurgi",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Pengolahan dan pemurnian bijih logam (smelter nikel, tembaga, bauksit), termodinamika ekstraksi pirometalurgi & hidrometalurgi, dan rekayasa korosi material industri.",
            "en": "Mineral processing and smelting metallurgy (nickel, copper, bauxite), pyrometallurgy, hydrometallurgy, and industrial corrosion engineering."
        },
        "fokus": {
            "id": ["Pengolahan Mineral & Smelter Ekstraksi Logam", "Hidrometalurgi & Pemurnian Nikel Baterai", "Pirometalurgi Suhu Tinggi & Peleburan", "Elektrokimia Korosi & Perlindungan Katodik"],
            "en": ["Mineral Processing & Smelting Metallurgy", "Hydrometallurgy for Battery-Grade Nickel", "High-Temperature Pyrometallurgy", "Corrosion Electrochemistry & Cathodic Protection"]
        },
        "karir": {
            "id": ["Smelter Operations Metallurgist", "Mineral Processing Plant Engineer", "Corrosion & Asset Integrity Specialist", "Battery Raw Materials Refining Lead"],
            "en": ["Smelter Metallurgical Engineer", "Mineral Processing Superintendent", "Corrosion Asset Integrity Lead", "Battery Materials Refining Specialist"]
        }
    },

    # =========================================================================
    # 5. FTSL - Fakultas Teknik Sipil dan Lingkungan (Ganesa & Jatinangor)
    # =========================================================================
    {
        "id": "s1-teknik-sipil",
        "kode": "15001",
        "nama": "Teknik Sipil",
        "nama_en": "Civil Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTSL-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknik Sipil dan Lingkungan", "fakultas_singkatan": "FTSL",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 130, "dt_snbp": 39, "dt_snbt": 52, "dt_smitb": 39,
        "website": "https://si.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Pendidikan teknik sipil tertua di nusantara, mencetak perancang megastruktur jembatan bentang panjang, gedung pencakar langit tahan gempa, dan infrastruktur transportasi massal.",
            "en": "Oldest civil engineering program in Indonesia, producing designers of long-span bridges, earthquake-proof skyscrapers, and rapid transit networks."
        },
        "fokus": {
            "id": ["Rekayasa Struktur Tahan Gempa Lanjut", "Geoteknik Pondasi Dalam & Terowongan", "Rekayasa Transportasi & Jalan Raya", "Manajemen Konstruksi & Pemodelan BIM"],
            "en": ["Advanced Earthquake Structural Engineering", "Deep Foundation Geotechnics & Tunneling", "Transportation Infrastructure Engineering", "BIM & Mega-Project Construction Management"]
        },
        "karir": {
            "id": ["Senior Structural Design Engineer", "Geotechnical & Tunneling Specialist", "Highway & Rail Transit Project Lead", "Chief Construction Project Manager"],
            "en": ["Structural Engineering Consultant", "Geotechnical & Tunnel Specialist", "Transit Infrastructure Lead", "Project Construction Director"]
        }
    },
    {
        "id": "s1-teknik-lingkungan",
        "kode": "15301",
        "nama": "Teknik Lingkungan",
        "nama_en": "Environmental Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTSL-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknik Sipil dan Lingkungan", "fakultas_singkatan": "FTSL",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 100, "dt_snbp": 30, "dt_snbt": 40, "dt_smitb": 30,
        "website": "https://tl.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Rekayasa instalasi pengolahan air minum, pengolahan air limbah industri canggih, pengendalian emisi udara, dan pengelolaan persampahan perkotaan sirkular.",
            "en": "Engineering of drinking water purification, industrial wastewater treatment (WWTP), air pollution control, and circular municipal solid waste."
        },
        "fokus": {
            "id": ["Pengolahan Air Minum & Air Limbah Lanjut", "Pengendalian Pencemaran Udara Industri", "Pengelolaan Sampah Terpadu & Circular Economy", "Analisis Dampak Lingkungan (AMDAL) Lanjut"],
            "en": ["Advanced Water & Wastewater Treatment", "Industrial Air Pollution Control Systems", "Circular Municipal Solid Waste Management", "Environmental Impact Assessment (EIA/AMDAL)"]
        },
        "karir": {
            "id": ["Environmental Plant Design Engineer", "Water & Wastewater Infrastructure Lead", "HSE & Environmental Auditor Industri", "Sustainable Sanitation Project Manager"],
            "en": ["Environmental Process Design Engineer", "Water Infrastructure Lead", "Industrial HSE / ESG Auditor", "Municipal Sanitation Director"]
        }
    },
    {
        "id": "s1-teknik-kelautan",
        "kode": "15501",
        "nama": "Teknik Kelautan",
        "nama_en": "Ocean Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTSL-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Teknik Sipil dan Lingkungan", "fakultas_singkatan": "FTSL",
        "akreditasi": "Unggul", "akreditasi_skor": "381",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 32, "dt_smitb": 24,
        "website": "https://kl.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Perancangan anjungan migas lepas pantai (offshore platform), pelabuhan laut dalam, energi gelombang & arus laut, dan perlindungan garis pantai dari abrasi.",
            "en": "Structural design of offshore oil/gas platforms, deepwater container ports, ocean wave/tidal energy, and coastal erosion defense engineering."
        },
        "fokus": {
            "id": ["Desain Struktur Lepas Pantai (Offshore Fixed/Floating)", "Hidrodinamika Gelombang Laut & Pasang Surut", "Perancangan Pelabuhan & Dermaga Laut Dalam", "Rekayasa Pantai & Energi Terbarukan Laut"],
            "en": ["Fixed & Floating Offshore Structural Design", "Ocean Wave Hydrodynamics & Metocean", "Deepwater Port & Jetty Engineering", "Coastal Protection & Marine Renewable Energy"]
        },
        "karir": {
            "id": ["Offshore Structural Engineer", "Subsea Pipeline & Port Design Engineer", "Marine Operations Specialist", "Coastal Defense Consultant"],
            "en": ["Offshore Structural Designer", "Port & Harbour Civil Engineer", "Marine Subsea Installation Lead", "Coastal Infrastructure Specialist"]
        }
    },
    {
        "id": "s1-rekayasa-infrastruktur-lingkungan",
        "kode": "15701",
        "nama": "Rekayasa Infrastruktur Lingkungan",
        "nama_en": "Environmental Infrastructure Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTSL-Jatinangor",
        "lokasi": "Kampus ITB Jatinangor (Sumedang)",
        "fakultas": "Fakultas Teknik Sipil dan Lingkungan", "fakultas_singkatan": "FTSL",
        "akreditasi": "Unggul", "akreditasi_skor": "376",
        "akreditasi_internasional": [],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 24, "dt_smitb": 18,
        "website": "https://ril.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Penyediaan infrastruktur air minum permukiman, sistem drainase perkotaan ramah lingkungan (sponge city), dan jaringan sanitasi terpadu.",
            "en": "Municipal potable water network planning, urban eco-drainage (sponge cities), and decentralized community sanitation infrastructure."
        },
        "fokus": {
            "id": ["Jaringan Pipa Distribusi Air Minum (PDAM)", "Drainase Perkotaan & Pengendalian Banjir", "Sanitasi Terdesentralisasi & Pengolahan Lumpur", "Manajemen Aset Infrastruktur Publik"],
            "en": ["Water Supply Distribution Systems", "Urban Flood Drainage & Sponge Cities", "Decentralized Sanitation Infrastructure", "Public Infrastructure Asset Management"]
        },
        "karir": {
            "id": ["Water Infrastructure Planning Engineer", "Drainage & Urban Hydrology Specialist", "Municipal Sanitation Project Officer", "Smart Water Network Analyst"],
            "en": ["Water Utility Infrastructure Engineer", "Urban Drainage Specialist", "Municipal Sanitation Director", "Smart Water Network Analyst"]
        }
    },

    # =========================================================================
    # 6. SAPPK - Arsitektur, Perencanaan & Kebijakan (Ganesa & Cirebon)
    # =========================================================================
    {
        "id": "s1-arsitektur",
        "kode": "15201",
        "nama": "Arsitektur",
        "nama_en": "Architecture",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "SAPPK-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Arsitektur, Perencanaan dan Pengembangan Kebijakan", "fakultas_singkatan": "SAPPK",
        "akreditasi": "Unggul", "akreditasi_skor": "385",
        "akreditasi_internasional": ["KAAB", "UIA"],
        "daya_tampung": 90, "dt_snbp": 27, "dt_snbt": 36, "dt_smitb": 27,
        "website": "https://ar.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Terakreditasi KAAB internasional, pendidikan arsitektur terkemuka dengan tradisi studio perancangan yang kuat, arsitektur tropis berkelanjutan, dan teknologi komputasi parametrik.",
            "en": "KAAB-accredited premier architecture department, renowned for rigorous design studios, bioclimatic tropical sustainability, and computational design."
        },
        "fokus": {
            "id": ["Studio Perancangan Arsitektur Komprehensif", "Arsitektur Tropis & Bangunan Rendah Karbon", "Teknologi Desain Parametrik & Digital Fabrication", "Sejarah, Teori, & Kritik Arsitektur"],
            "en": ["Comprehensive Architectural Studios", "Tropical Bioclimatic Architecture", "Parametric Computational Design", "Architectural History & Theory"]
        },
        "karir": {
            "id": ["Principal Architect di Konsultan Arsitektur", "Green Building Design Consultant", "BIM Specialist & Parametric Modeler", "Urban Spatial & Heritage Designer"],
            "en": ["Principal Architectural Designer", "Green Building Sustainability Consultant", "Computational BIM Specialist", "Urban Architectural Designer"]
        }
    },
    {
        "id": "s1-perencanaan-wilayah-dan-kota",
        "kode": "15401",
        "nama": "Perencanaan Wilayah dan Kota",
        "nama_en": "Urban and Regional Planning (Planology)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "SAPPK-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Arsitektur, Perencanaan dan Pengembangan Kebijakan", "fakultas_singkatan": "SAPPK",
        "akreditasi": "Unggul", "akreditasi_skor": "383",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 85, "dt_snbp": 25, "dt_snbt": 34, "dt_smitb": 26,
        "website": "https://pl.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Perencanaan tata ruang kota modern, analisis sistem transportasi publik, pencegahan pemukiman kumuh, dan pengembangan wilayah kepulauan berkelanjutan.",
            "en": "Urban spatial masterplanning, public transit network optimization, sustainable settlements, and regional economic geography."
        },
        "fokus": {
            "id": ["Studio Perencanaan Kota & Masterplan Kawasan", "Sistem Informasi Geografis (GIS) & Spatial Big Data", "Perencanaan Transportasi Perkotaan Berkelanjutan", "Kebijakan Pembangunan Wilayah & Daerah"],
            "en": ["Urban Planning Studios & Masterplanning", "Geographic Information Systems (GIS)", "Urban Sustainable Transit Planning", "Regional Development Policy"]
        },
        "karir": {
            "id": ["Urban & Regional Planner di Bappenas / Kementerian ATR", "Konsultan Masterplan Kota & Real Estate", "Transport Planning Specialist", "Spatial Data Science Analyst"],
            "en": ["Urban & Regional Planner", "City Masterplanning Consultant", "Urban Transport Planner", "Spatial Big Data Analyst"]
        }
    },

    # =========================================================================
    # 7. FMIPA - Matematika & Ilmu Pengetahuan Alam (Ganesa)
    # =========================================================================
    {
        "id": "s1-matematika",
        "kode": "10101",
        "nama": "Matematika",
        "nama_en": "Mathematics",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FMIPA-M (Matematika)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "akreditasi": "Unggul", "akreditasi_skor": "383",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 90, "dt_snbp": 27, "dt_snbt": 36, "dt_smitb": 27,
        "website": "https://math.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Fondasi analisis matematika abstrak, aljabar modern, pemodelan stokastik, dan matematika optimasi untuk sains dan teknologi tingkat tinggi.",
            "en": "Mathematical foundations covering abstract analysis, modern algebra, stochastic modeling, and optimization algorithms for high-tech applications."
        },
        "fokus": {
            "id": ["Aljabar Abstrak & Analisis Matematis Murni", "Pemodelan Matematika Sistem Kompleks", "Matematika Keuangan & Optimasi Stokastik", "Statistika Matematika & Sains Data"],
            "en": ["Abstract Algebra & Real Analysis", "Mathematical Dynamic Systems Modeling", "Quantitative Finance & Optimization", "Mathematical Statistics & Data Science"]
        },
        "karir": {
            "id": ["Quantitative Analyst (Quant) di Finansial", "Machine Learning Algorithm Scientist", "Data Scientist di Korporasi Teknologi", "Peneliti Matematika Murni & Terapan"],
            "en": ["Quantitative Financial Strategist", "Machine Learning Modeler", "Enterprise Data Scientist", "Applied Mathematics Researcher"]
        }
    },
    {
        "id": "s1-aktuaria",
        "kode": "10801",
        "nama": "Aktuaria",
        "nama_en": "Actuarial Science",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FMIPA-M (Matematika)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 55, "dt_snbp": 16, "dt_snbt": 22, "dt_smitb": 17,
        "website": "https://actuary.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Program studi berpersaingan ketat, memadukan matematika probabilitas tingkat tinggi, valuasi risiko asuransi, pemodelan solvabilitas, dan dana pensiun.",
            "en": "Hyper-competitive program synthesizing advanced probability, insurance risk valuation, solvency modeling, and pension schemes."
        },
        "fokus": {
            "id": ["Matematika Asuransi Jiwa & Kesehatan", "Teori Risiko & Valuasi Cadangan Klaim", "Matematika Finansial & Portofolio Investasi", "Pemodelan Manajemen Solvabilitas"],
            "en": ["Life & Health Insurance Mathematics", "Risk Theory & Claim Loss Reserving", "Financial Mathematics & Investments", "Solvency Capital Modeling"]
        },
        "karir": {
            "id": ["Aktuaris Bersertifikasi (FSAI / ASAI)", "Financial Risk Manager (FRM)", "Underwriting & Pricing Specialist Asuransi", "Konsultan Manajemen Dana Pensiun"],
            "en": ["Certified Actuary (FSAI/ASAI)", "Financial Risk Manager (FRM)", "Insurance Pricing Specialist", "Pension Fund Investment Consultant"]
        }
    },
    {
        "id": "s1-fisika",
        "kode": "10201",
        "nama": "Fisika",
        "nama_en": "Physics",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FMIPA-IPA (Ilmu Pengetahuan Alam)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "akreditasi": "Unggul", "akreditasi_skor": "381",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 90, "dt_snbp": 27, "dt_snbt": 36, "dt_smitb": 27,
        "website": "https://fi.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Mengkaji fenomena alam fundamental, fisika kuantum komputasi, fisika material elektronik, fisika nuklir terapan, dan biofisika molekuler.",
            "en": "Examines fundamental physical phenomena, computational quantum physics, electronic materials, applied nuclear physics, and molecular biophysics."
        },
        "fokus": {
            "id": ["Mekanika Kuantum & Elektrodinamika Klasik", "Fisika Komputasi & Simulasi Material", "Fisika Nuklir & Reaktor Terapan", "Biofisika & Nanoteknologi"],
            "en": ["Quantum Mechanics & Electrodynamics", "Computational Materials Physics", "Nuclear Physics & Radiation Technology", "Biophysics & Nanostructures"]
        },
        "karir": {
            "id": ["Peneliti Fisika Badan Riset (BRIN / BATAN)", "Semiconductor & Materials Scientist", "Computational Modeler di Riset Industri", "Dosen & Akademisi Sains Fisika"],
            "en": ["Nuclear & Energy Research Scientist", "Semiconductor Device Scientist", "Scientific Computational Modeler", "Physics University Faculty"]
        }
    },
    {
        "id": "s1-astronomi",
        "kode": "10301",
        "nama": "Astronomi",
        "nama_en": "Astronomy and Astrophysics",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FMIPA-IPA (Ilmu Pengetahuan Alam)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 45, "dt_snbp": 13, "dt_snbt": 18, "dt_smitb": 14,
        "website": "https://as.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Satu-satunya program studi astronomi di Asia Tenggara, meneliti astrofisika bintang, kosmologi evolusi alam semesta, mekanika benda langit, dan instrumen observatorium Bosscha.",
            "en": "The only astronomy department in Southeast Asia, studying stellar astrophysics, cosmology, orbital celestial mechanics, and Bosscha Observatory operations."
        },
        "fokus": {
            "id": ["Astrofisika Teoretik & Komputasi Bintang", "Kosmologi & Evolusi Galaksi", "Astronomi Observasi & Pengolahan Citra Teleskop", "Tata Surya & Fisika Benda Antariksa"],
            "en": ["Theoretical & Computational Astrophysics", "Cosmology & Extragalactic Astronomy", "Observational Astronomy & Telescope Imaging", "Solar System & Planetary Dynamics"]
        },
        "karir": {
            "id": ["Astrofisikawan & Peneliti Antariksa (BRIN / NASA / ESO)", "Data Scientist Pengolahan Citra & Big Data", "Peneliti Observatorium Astronomi", "Pendidik & Edukator Sains Antariksa"],
            "en": ["Space & Astrophysics Scientist", "Astronomical Big Data Scientist", "Observatory Research Specialist", "Space Science Communicator"]
        }
    },
    {
        "id": "s1-kimia",
        "kode": "10501",
        "nama": "Kimia",
        "nama_en": "Chemistry",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FMIPA-IPA (Ilmu Pengetahuan Alam)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Matematika dan Ilmu Pengetahuan Alam", "fakultas_singkatan": "FMIPA",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["RSC", "ASIIN"],
        "daya_tampung": 90, "dt_snbp": 27, "dt_snbt": 36, "dt_smitb": 27,
        "website": "https://chem.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Terakreditasi internasional Royal Society of Chemistry (RSC), mendalami sintesis molekul organik maju, kimia analitik instrumentasi modern, dan biokimia hayati.",
            "en": "RSC-accredited department advancing modern organic synthesis, instrumental analytical chemistry, and chemical biology."
        },
        "fokus": {
            "id": ["Sintesis Organik & Bahan Obat", "Kimia Material Anorganik & Katalis", "Kimia Analitik Spektroskopi Modern", "Biokimia & Rekayasa Enzimatik"],
            "en": ["Organic Synthesis & Pharmaceutical Chemistry", "Inorganic Materials & Catalysts", "Advanced Analytical Spectroscopy", "Biochemistry & Enzymatic Engineering"]
        },
        "karir": {
            "id": ["R&D Chemist di Industri Kimia & Farmasi", "Analis Laboratorium Forensik & Pengujian Mutu", "Chemical Quality Assurance Specialist", "Peneliti Kimia Material & Energi Bersih"],
            "en": ["Industrial Chemical R&D Chemist", "Forensic & Regulatory Chemist", "Quality Assurance Chemistry Lead", "Clean Energy Materials Chemist"]
        }
    },

    # =========================================================================
    # 8. SITH - Ilmu & Teknologi Hayati (Ganesa & Jatinangor)
    # =========================================================================
    {
        "id": "s1-biologi",
        "kode": "10601",
        "nama": "Biologi",
        "nama_en": "Biology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "SITH-S (Sains)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Ilmu dan Teknologi Hayati", "fakultas_singkatan": "SITH",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 32, "dt_smitb": 24,
        "website": "https://sith.itb.ac.id/biologi",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Eksplorasi biologi molekuler, genetika organisme tropis, ekologi konservasi biodiversitas, dan interaksi fisiologi organisme hidup.",
            "en": "Exploration of molecular biology, tropical organism genetics, biodiversity conservation, and organismal physiology."
        },
        "fokus": {
            "id": ["Biologi Molekuler & Genetika Populasi", "Ekologi Biodiversitas & Konservasi Alam", "Fisiologi Organisme Tropis", "Biosistematika & Bioinformatika"],
            "en": ["Molecular Biology & Population Genetics", "Biodiversity Ecology & Conservation", "Tropical Organism Physiology", "Biosystematics & Bioinformatics"]
        },
        "karir": {
            "id": ["Peneliti Biologi Molekuler (BRIN / Lembaga Riset)", "Konservasionis & Spesialis Ekologi Lingkungan", "Bioinformatician & Data Analyst", "Konsultan Pengelolaan Sumber Daya Hayati"],
            "en": ["Molecular Biology Scientist", "Wildlife Conservation Specialist", "Bioinformatics Data Analyst", "Ecological Resource Consultant"]
        }
    },
    {
        "id": "s1-mikrobiologi",
        "kode": "10401",
        "nama": "Mikrobiologi",
        "nama_en": "Microbiology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "SITH-S (Sains)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Ilmu dan Teknologi Hayati", "fakultas_singkatan": "SITH",
        "akreditasi": "Unggul", "akreditasi_skor": "379",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 24, "dt_smitb": 18,
        "website": "https://sith.itb.ac.id/mikro",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Kajian mikroorganisme bakteri, virus, kapang, dan jamur untuk produksi pangan fermentasi, antibiotik farmasi, bioremediasi limbah, dan virologi.",
            "en": "Examines bacteria, viruses, and fungi for fermented food processing, pharmaceutical antibiotics, waste bioremediation, and industrial microbiology."
        },
        "fokus": {
            "id": ["Mikrobiologi Industri & Fermentasi", "Virologi & Imunologi Mikrobial", "Bioremediasi Lingkungan oleh Mikroba", "Genomika & Rekayasa Genetik Mikroba"],
            "en": ["Industrial Fermentation Microbiology", "Virology & Microbial Immunology", "Environmental Bioremediation Mechanics", "Microbial Genomics & Genetic Editing"]
        },
        "karir": {
            "id": ["Industrial Microbiologist (Industri Makanan/Vaksin)", "Quality Control & Assurance Microbiologist", "Bioremediation & Waste Treatment Specialist", "Virology Research Scientist"],
            "en": ["Industrial Microbiologist (Pharma/Food)", "QC Microbiological Specialist", "Bioremediation Environmental Lead", "Virology Research Scientist"]
        }
    },
    {
        "id": "s1-rekayasa-hayati",
        "kode": "11201",
        "nama": "Rekayasa Hayati",
        "nama_en": "Bioengineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "SITH-R (Rekayasa)",
        "lokasi": "Kampus ITB Jatinangor (Sumedang)",
        "fakultas": "Sekolah Ilmu dan Teknologi Hayati", "fakultas_singkatan": "SITH",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ABET", "ASIIN"],
        "daya_tampung": 70, "dt_snbp": 21, "dt_snbt": 28, "dt_smitb": 21,
        "website": "https://sith.itb.ac.id/hayati",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Terakreditasi ABET, menerapkan prinsip teknik pada sistem biologis untuk memproduksi biomaterial terbarukan, biokatalisis, dan industri bio-manufaktur modern.",
            "en": "ABET-accredited bioengineering applying engineering to biological systems for renewable biomaterials, biocatalysis, and biomanufacturing."
        },
        "fokus": {
            "id": ["Bioproses & Operasi Bioreaktor Lanjut", "Rekayasa Sintetik Biologis & Biokatalisis", "Downstream Processing Produk Hayati", "Perancangan Industri Berbasis Hayati"],
            "en": ["Advanced Bioreactor Engineering", "Synthetic Biology & Biocatalysis", "Downstream Bioprocess Separation", "Bio-Based Industrial Facility Design"]
        },
        "karir": {
            "id": ["Bioengineering Process Engineer", "Biomanufacturing Plant Operations Lead", "Industrial Synthetic Biology Researcher", "Bioproduct Regulatory Specialist"],
            "en": ["Bioengineering Process Engineer", "Biomanufacturing Operations Lead", "Synthetic Biology Research Scientist", "Bioproduct Regulatory Specialist"]
        }
    },
    {
        "id": "s1-rekayasa-pertanian",
        "kode": "11401",
        "nama": "Rekayasa Pertanian",
        "nama_en": "Agricultural Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "SITH-R (Rekayasa)",
        "lokasi": "Kampus ITB Jatinangor (Sumedang)",
        "fakultas": "Sekolah Ilmu dan Teknologi Hayati", "fakultas_singkatan": "SITH",
        "akreditasi": "Unggul", "akreditasi_skor": "378",
        "akreditasi_internasional": ["ABET", "ASIIN"],
        "daya_tampung": 65, "dt_snbp": 20, "dt_snbt": 26, "dt_smitb": 19,
        "website": "https://sith.itb.ac.id/pertanian",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Pertanian presisi modern berbasis sensor Internet of Things (IoT), otomatisasi irigasi pintar, rekayasa biosistem tanaman, dan mekanisasi pascapanen.",
            "en": "Precision agriculture integrating IoT smart sensors, automated irrigation, plant biosystems, and post-harvest mechanization."
        },
        "fokus": {
            "id": ["Pertanian Presisi (Precision Farming & IoT)", "Rekayasa Hidrologi & Irigasi Pertanian Pintar", "Mekanika Tanah & Mesin Pertanian Otomatis", "Rekayasa Lingkungan Rumah Kaca (Greenhouse)"],
            "en": ["Precision Farming & Smart Sensor IoT", "Agricultural Irrigation & Water Management", "Automated Agricultural Machinery", "Controlled Environment Agriculture"]
        },
        "karir": {
            "id": ["Smart Agriculture Systems Engineer", "Precision Farming Agritech Lead", "Greenhouse Automation Specialist", "Agricultural Supply Chain Engineer"],
            "en": ["Precision Agriculture Systems Engineer", "Agritech Startup Technology Lead", "Controlled Environment Specialist", "Agri-Food Supply Chain Lead"]
        }
    },
    {
        "id": "s1-rekayasa-kehutanan",
        "kode": "11501",
        "nama": "Rekayasa Kehutanan",
        "nama_en": "Forestry Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "SITH-R (Rekayasa)",
        "lokasi": "Kampus ITB Jatinangor (Sumedang)",
        "fakultas": "Sekolah Ilmu dan Teknologi Hayati", "fakultas_singkatan": "SITH",
        "akreditasi": "Unggul", "akreditasi_skor": "377",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 24, "dt_smitb": 18,
        "website": "https://sith.itb.ac.id/kehutanan",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Manajemen hutan lestari berkelanjutan, rekayasa biomaterial kayu & serat alam, inventarisasi hutan berbasis drone lidar satelit, dan proyek kredit karbon hutan.",
            "en": "Sustainable forest management, bio-composites, drone lidar forest inventory, and forest carbon credit project verification."
        },
        "fokus": {
            "id": ["Silvikultur & Rekayasa Pemanenan Hutan Lestari", "Teknologi Biomaterial Kayu & Serat Alam", "Penginderaan Jauh & LiDAR Hutan", "Perhitungan Karbon Hutan & Proyek REDD+"],
            "en": ["Silviculture & Sustainable Forest Harvesting", "Wood & Bio-Based Composite Engineering", "Remote Sensing & Drone LiDAR Forestry", "Forest Carbon Accounting (REDD+)"]
        },
        "karir": {
            "id": ["Forestry Project Operations Manager", "Forest Carbon Credit & ESG Specialist", "Timber & Bio-Composites Engineer", "Spatial Forestry LiDAR Analyst"],
            "en": ["Forestry Operations Director", "Forest Carbon & ESG Project Lead", "Wood Biomaterials Engineer", "LiDAR Forest Spatial Analyst"]
        }
    },

    # =========================================================================
    # 9. SF - Sekolah Farmasi (Ganesa)
    # =========================================================================
    {
        "id": "s1-sains-dan-teknologi-farmasi",
        "kode": "11601",
        "nama": "Sains dan Teknologi Farmasi",
        "nama_en": "Pharmaceutical Science and Technology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "SF (Sekolah Farmasi)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Farmasi", "fakultas_singkatan": "SF",
        "akreditasi": "Unggul", "akreditasi_skor": "383",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 75, "dt_snbp": 22, "dt_snbt": 30, "dt_smitb": 23,
        "website": "https://fa.itb.ac.id/stf",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Spesialisasi riset kimia medisinal sintesis obat, teknologi penghantaran obat partikel nano (nanomedicine), dan pengembangan fitofarmaka bahan alam nusantara.",
            "en": "Specializes in medicinal chemistry, nanomedicine drug delivery systems, and phytopharmaceutical development from Indonesian natural bio-resources."
        },
        "fokus": {
            "id": ["Desain Obat Komputasi & Kimia Medisinal", "Teknologi Formulasi Sediaan & Nanomedicine", "Farmakologi & Uji Bioavailabilitas", "Isolasi Senyawa Bioaktif Bahan Alam"],
            "en": ["Computational Drug Design & Medicinal Chemistry", "Nanomedicine Formulation Technology", "Pharmacology & Bioavailability Screening", "Natural Product Bioactive Isolation"]
        },
        "karir": {
            "id": ["Formulation R&D Scientist Industri Farmasi", "Analytical Chemistry Quality Control Specialist", "Natural Medicine Product Developer", "Pharmaceutical Regulatory Specialist"],
            "en": ["Pharmaceutical Formulation Scientist", "Analytical Drug Quality Specialist", "Natural Medicine R&D Lead", "Pharma Regulatory Affairs Manager"]
        }
    },
    {
        "id": "s1-farmasi-klinik-dan-komunitas",
        "kode": "11701",
        "nama": "Farmasi Klinik dan Komunitas",
        "nama_en": "Clinical and Community Pharmacy",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "SF (Sekolah Farmasi)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Farmasi", "fakultas_singkatan": "SF",
        "akreditasi": "Unggul", "akreditasi_skor": "381",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 65, "dt_snbp": 20, "dt_snbt": 26, "dt_smitb": 19,
        "website": "https://fa.itb.ac.id/fkk",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Berfokus pada pelayanan farmasi klinis di rumah sakit, pemantauan terapi obat pasien (TDM), farmakoterapi penyakit kronis, dan manajemen apotek komunitas.",
            "en": "Focuses on hospital clinical pharmacy services, Therapeutic Drug Monitoring (TDM), chronic disease pharmacotherapy, and community pharmacy management."
        },
        "fokus": {
            "id": ["Farmakoterapi Klinis Terapan", "Therapeutic Drug Monitoring (TDM)", "Farmasi Rumah Sakit & Keselamatan Pasien", "Farmakoekonomi & Manajemen Apotek"],
            "en": ["Applied Clinical Pharmacotherapy", "Therapeutic Drug Monitoring", "Hospital Pharmacy & Patient Safety", "Pharmacoeconomics & Community Practice"]
        },
        "karir": {
            "id": ["Apoteker Klinis Rumah Sakit", "Clinical Research Associate (Uji Klinis)", "Medical Affairs Liaison di Farmasi Global", "Manajer Apotek & Layanan Pasien"],
            "en": ["Hospital Clinical Pharmacist", "Clinical Trial Research Associate", "Medical Affairs Specialist", "Community Pharmacy Practice Lead"]
        }
    },

    # =========================================================================
    # 10. FSRD - Fakultas Seni Rupa dan Desain (Ganesa & Cirebon)
    # =========================================================================
    {
        "id": "s1-desain-komunikasi-visual",
        "kode": "17401",
        "nama": "Desain Komunikasi Visual",
        "nama_en": "Visual Communication Design (Graphic Design)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Seni & Desain",
        "tpb_fakultas": "FSRD-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Seni Rupa dan Desain", "fakultas_singkatan": "FSRD",
        "akreditasi": "Unggul", "akreditasi_skor": "384",
        "akreditasi_internasional": [],
        "daya_tampung": 85, "dt_snbp": 25, "dt_snbt": 34, "dt_smitb": 26,
        "website": "https://fsrd.itb.ac.id/dkv",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Program studi DKV paling berpengaruh di Indonesia, menggabungkan identitas visual brand, tipografi mutakhir, desain interaksi UI/UX, dan narasi animasi sinematik.",
            "en": "Indonesia's most influential visual communication design school, combining brand identity, typography, UI/UX interaction, and cinematic animation."
        },
        "fokus": {
            "id": ["Identitas Visual Branding & Tipografi Lanjut", "Desain Interaksi UI/UX & Produk Digital", "Ilustrasi Naratif & Desain Karakter", "Animasi Komersial & Desain Gerak (Motion)"],
            "en": ["Brand Identity Systems & Advanced Typography", "UI/UX Interaction & Digital Product Design", "Narrative Illustration & Character Design", "Commercial Motion Graphics & Animation"]
        },
        "karir": {
            "id": ["Creative Director di Agensi Desain Global", "Lead UI/UX & Digital Product Designer", "Brand Identity Strategist", "Senior Motion Designer / Art Director"],
            "en": ["Creative Director at Global Agencies", "Lead UI/UX Product Designer", "Brand Identity Strategist", "Senior Motion Graphics Director"]
        }
    },
    {
        "id": "s1-desain-produk",
        "kode": "17501",
        "nama": "Desain Produk",
        "nama_en": "Industrial Product Design",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Seni & Desain",
        "tpb_fakultas": "FSRD-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Seni Rupa dan Desain", "fakultas_singkatan": "FSRD",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": [],
        "daya_tampung": 65, "dt_snbp": 20, "dt_snbt": 26, "dt_smitb": 19,
        "website": "https://fsrd.itb.ac.id/desain-produk",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Perancangan produk industri manufaktur, desain kendaraan transportasi, perabot furnitur inovatif, dan perangkat elektronik ramah pengguna.",
            "en": "Design of manufactured consumer products, automotive transportation styling, furniture ergonomics, and user-centered hardware devices."
        },
        "fokus": {
            "id": ["Studio Perancangan Produk Konsumen", "Desain Transportasi & Ergonomi Otomotif", "Desain Furnitur & Material Berkelanjutan", "Prototyping Cepat & Pemodelan 3D CAD"],
            "en": ["Consumer Hardware Product Studios", "Automotive Transportation Styling", "Sustainable Furniture & Lighting Design", "Rapid Prototyping & 3D Surface CAD"]
        },
        "karir": {
            "id": ["Industrial Product Designer", "Automotive & Transportation Exterior Designer", "Furniture & Lighting Designer", "Hardware Consumer Experience Lead"],
            "en": ["Industrial Product Designer", "Automotive Exterior Styling Lead", "Furniture & Lifestyle Product Designer", "Hardware Design Strategist"]
        }
    },
    {
        "id": "s1-desain-interior",
        "kode": "17301",
        "nama": "Desain Interior",
        "nama_en": "Interior Design",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Seni & Desain",
        "tpb_fakultas": "FSRD-Ganesa",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Seni Rupa dan Desain", "fakultas_singkatan": "FSRD",
        "akreditasi": "Unggul", "akreditasi_skor": "378",
        "akreditasi_internasional": [],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 24, "dt_smitb": 18,
        "website": "https://fsrd.itb.ac.id/interior",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Tata ruang interior hunian, ruang publik komersial, perhotelan mewah, tata cahaya interior, dan psikologi lingkungan ruang dalam.",
            "en": "Spatial design of residences, commercial retail hubs, luxury hospitality venues, interior illumination, and environmental psychology."
        },
        "fokus": {
            "id": ["Studio Perancangan Interior Komersial & Residensial", "Tata Cahaya & Akustik Interior", "Bahan Bangunan Interior & Konstruksi Detail", "Psikologi Ruang & Estetika Lingkungan"],
            "en": ["Commercial & Residential Interior Studios", "Interior Lighting & Architectural Acoustics", "Detail Interior Joinery Construction", "Spatial Psychology & Environmental Aesthetics"]
        },
        "karir": {
            "id": ["Interior Design Consultant", "Hospitality & Retail Space Designer", "Architectural Lighting Designer", "Exhibition & Museum Space Designer"],
            "en": ["Professional Interior Designer", "Hospitality Interior Specialist", "Architectural Lighting Consultant", "Exhibition Spatial Designer"]
        }
    },

    # =========================================================================
    # 11. SBM - Sekolah Bisnis dan Manajemen (Ganesa & Jatinangor)
    # =========================================================================
    {
        "id": "s1-manajemen",
        "kode": "19001",
        "nama": "Manajemen",
        "nama_en": "Management",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Bisnis & Manajemen",
        "tpb_fakultas": "SBM",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Bisnis dan Manajemen", "fakultas_singkatan": "SBM",
        "akreditasi": "Unggul", "akreditasi_skor": "385",
        "akreditasi_internasional": ["AACSB"],
        "daya_tampung": 180, "dt_snbp": 54, "dt_snbt": 72, "dt_smitb": 54,
        "website": "https://sbm.itb.ac.id",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 14.500.000)",
        "deskripsi": {
            "id": "Sekolah bisnis terakreditasi AACSB internasional, melahirkan pemimpin korporasi dengan kurikulum integrasi kepemimpinan berbasis aksi, keuangan strategis, pemasaran digital, dan operasi global.",
            "en": "AACSB-accredited premier business school preparing future executive leaders across corporate finance, action-based leadership, digital marketing, and operations."
        },
        "fokus": {
            "id": ["Kepemimpinan Berbasis Aksi & Etika Bisnis", "Manajemen Keuangan Korporasi & Valuasi", "Pemasaran Strategis & Pertumbuhan Digital", "Operasional Bisnis & Manajemen Talenta"],
            "en": ["Action-Based Leadership & Governance", "Corporate Financial Strategy & Valuation", "Strategic Marketing & Digital Growth", "Global Business Operations & Talent Systems"]
        },
        "karir": {
            "id": ["Management Consultant (McKinsey/BCG/Bain)", "Investment Banker / Equity Research Analyst", "Global FMCG Leadership Trainee", "Corporate Strategic Business Development"],
            "en": ["Strategy Management Consultant", "Investment Banking Analyst", "Global FMCG Management Trainee", "Corporate Strategy & Business Development"]
        }
    },
    {
        "id": "s1-kewirausahaan",
        "kode": "19201",
        "nama": "Kewirausahaan",
        "nama_en": "Entrepreneurship",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Bisnis & Manajemen",
        "tpb_fakultas": "SBM",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Bisnis dan Manajemen", "fakultas_singkatan": "SBM",
        "akreditasi": "Unggul", "akreditasi_skor": "381",
        "akreditasi_internasional": ["AACSB"],
        "daya_tampung": 75, "dt_snbp": 22, "dt_snbt": 30, "dt_smitb": 23,
        "website": "https://sbm.itb.ac.id/entrepreneurship",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 14.500.000)",
        "deskripsi": {
            "id": "Inkubator wirausaha bergelar sarjana, membimbing mahasiswa membangun, menguji validasi pasar, dan mengeksekusi startup rintisan secara langsung selama perkuliahan.",
            "en": "Venture incubator bachelor program guiding students to conceptualize, market-validate, scale, and fund real commercial startup ventures."
        },
        "fokus": {
            "id": ["Validasi Pasar & Eksplorasi Peluang Bisnis", "Pengembangan Model Bisnis Rintisan (Lean Startup)", "Pendanaan Modal Ventura & Negosiasi Pitching", "Skalabilitas Bisnis & Ekspansi Operasional"],
            "en": ["Market Opportunity Validation", "Lean Startup Modeling & Customer Discovery", "Venture Capital Fundraising & Pitching", "Business Scaling & Growth Operations"]
        },
        "karir": {
            "id": ["Startup Founder / CEO Rintisan Teknologi", "Venture Capital Associate / Investment Analyst", "Corporate Innovation & Intrapreneurship Lead", "Business Scaling & Accelerator Mentor"],
            "en": ["Tech Startup Founder / CEO", "Venture Capital Investment Associate", "Corporate Venture Innovation Lead", "Accelerator Program Lead"]
        }
    },

    # =========================================================================
    # FITB - Fakultas Ilmu dan Teknologi Kebumian (Ganesa)
    # =========================================================================
    {
        "id": "s1-teknik-geologi",
        "kode": "12001",
        "nama": "Teknik Geologi",
        "nama_en": "Geological Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FITB-G (Ganesa)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Ilmu dan Teknologi Kebumian", "fakultas_singkatan": "FITB",
        "akreditasi": "Unggul", "akreditasi_skor": "380",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 120, "dt_snbp": 36, "dt_snbt": 48, "dt_smitb": 36,
        "website": "https://fitb.itb.ac.id/geologi",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Eksplorasi struktur dan dinamika bumi, identifikasi cadangan mineral, mitigasi bahaya geologi (gempa dan gunung api), serta geologi teknik infrastruktur.",
            "en": "Exploration of Earth crustal dynamics, mineral resource evaluation, geological disaster mitigation, and geotechnical infrastructure engineering."
        },
        "fokus": {
            "id": ["Geologi Struktur & Tektonika Lempeng", "Petrologi & Sedimentologi Migas", "Geologi Tata Lingkungan & Bencana Alam", "Eksplorasi Sumber Daya Mineral & Batubara"],
            "en": ["Structural Geology & Plate Tectonics", "Petrology & Petroleum Sedimentology", "Environmental & Engineering Geology", "Mineral and Coal Resource Exploration"]
        },
        "karir": {
            "id": ["Exploration Geologist di Sektor Energi & Pertambangan", "Geotechnical Engineer Proyek Infrastruktur Strategis", "Peneliti Vulkanologi & Seismologi Badan Geologi / BMKG", "Konsultan AMDAL & Hidrogeologi Air Tanah"],
            "en": ["Exploration Geologist in Energy & Mining", "Geotechnical Engineer for Civil Mega-projects", "Volcanology & Seismology Researcher at BMKG/PVMBG", "Hydrogeology & Environmental Consultant"]
        }
    },
    {
        "id": "s1-teknik-geodesi-dan-geomatika",
        "kode": "15101",
        "nama": "Teknik Geodesi dan Geomatika",
        "nama_en": "Geodesy and Geomatics Engineering",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FITB-G (Ganesa)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Ilmu dan Teknologi Kebumian", "fakultas_singkatan": "FITB",
        "akreditasi": "Unggul", "akreditasi_skor": "382",
        "akreditasi_internasional": ["ABET", "IABEE"],
        "daya_tampung": 120, "dt_snbp": 36, "dt_snbt": 48, "dt_smitb": 36,
        "website": "https://fitb.itb.ac.id/gd",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Penentuan posisi spasial presisi tinggi, pemodelan geoid bumi, fotogrametri satelit, teknologi drone LiDAR, dan sistem informasi geografis (GIS) 3D.",
            "en": "High-precision satellite positioning, geoid modeling, UAV photogrammetry, airborne LiDAR mapping, and 3D geospatial information systems."
        },
        "fokus": {
            "id": ["Satelit Geodesi & Penentuan Posisi GNSS", "Fotogrametri Digital & Penginderaan Jauh LiDAR", "Sistem Informasi Geografis & Spatial Data Science", "Kadaster & Pemetaan Batas Wilayah Nasional"],
            "en": ["Satellite Geodesy & GNSS Positioning", "Digital Photogrammetry & Remote Sensing LiDAR", "Geographic Information Systems & Spatial Data Science", "Cadastral Surveying & Boundary Delimitation"]
        },
        "karir": {
            "id": ["Geomatics Engineer & Drone Surveyor Lead", "Spatial Data Scientist & GIS Architect di Perusahaan Big Tech", "Surveyor Ahli Kadaster & Tata Ruang ATR/BPN", "Hydrographic Surveyor Offshore Drilling"],
            "en": ["Geomatics Engineer & UAV Surveyor Lead", "Spatial Data Scientist & GIS Architect", "Cadastral Surveyor at ATR/BPN", "Offshore Hydrographic Surveyor"]
        }
    },
    {
        "id": "s1-meteorologi",
        "kode": "12801",
        "nama": "Meteorologi",
        "nama_en": "Meteorology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FITB-G (Ganesa)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Ilmu dan Teknologi Kebumian", "fakultas_singkatan": "FITB",
        "akreditasi": "Unggul", "akreditasi_skor": "376",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 32, "dt_smitb": 24,
        "website": "https://fitb.itb.ac.id/me",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Pemodelan numerik atmosfer benua maritim, dinamika cuaca ekstrem, prediksi perubahan iklim global, dan rekayasa energi terbarukan angin dan surya.",
            "en": "Atmospheric numerical modeling in the maritime continent, extreme weather dynamics, climate change projection, and wind/solar energy forecasting."
        },
        "fokus": {
            "id": ["Dinamika Atmosfer & Termodinamika Cuaca", "Pemodelan Numerik Cuaca & Prediksi Iklim", "Meteorologi Radar & Satelit Cuaca", "Meteorologi Lingkungan & Kualitas Udara"],
            "en": ["Atmospheric Dynamics & Thermodynamics", "Numerical Weather Prediction & Climate Modeling", "Radar & Satellite Meteorology", "Environmental Meteorology & Air Quality Modeling"]
        },
        "karir": {
            "id": ["Meteorologis & Analis Cuaca Penerbangan BMKG", "Climate Risk & Renewable Energy Consultant", "Data Scientist Pemodelan Iklim & Bencana Hidrometeorologi", "Penyelidik Kualitas Udara & Polusi Lingkungan"],
            "en": ["Aviation Meteorologist & Forecaster at BMKG", "Climate Risk & Renewable Energy Consultant", "Climate Modeling Data Scientist", "Air Quality & Pollution Analyst"]
        }
    },
    {
        "id": "s1-oseanografi",
        "kode": "12901",
        "nama": "Oseanografi",
        "nama_en": "Oceanography",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FITB-G (Ganesa)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Ilmu dan Teknologi Kebumian", "fakultas_singkatan": "FITB",
        "akreditasi": "Unggul", "akreditasi_skor": "375",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 80, "dt_snbp": 24, "dt_snbt": 32, "dt_smitb": 24,
        "website": "https://fitb.itb.ac.id/os",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Studi komprehensif dinamika laut, arus lintas Indonesia (ARLINDO), pasang surut, gelombang laut dalam, serta pemodelan lingkungan maritim dan pesisir.",
            "en": "Comprehensive physical and biogeochemical ocean dynamics, Indonesian Throughflow, tidal mechanics, wave modeling, and coastal ecosystem preservation."
        },
        "fokus": {
            "id": ["Dinamika Arus Laut & Interaksi Laut-Atmosfer", "Pemodelan Numerik Sirkulasi Laut & Gelombang", "Oseanografi Akustik & Eksplorasi Bawah Laut", "Mitigasi Abrasi & Rekayasa Pesisir Maritim"],
            "en": ["Ocean Circulation & Air-Sea Interaction", "Numerical Wave & Hydrodynamic Modeling", "Underwater Acoustics & Subsea Exploration", "Coastal Dynamics & Marine Hazard Mitigation"]
        },
        "karir": {
            "id": ["Oceanographic Engineer di Industri Migas Lepas Pantai (Offshore)", "Analis Pemodelan Kelautan & Tsunami BMKG / BRIN", "Konsultan Rekayasa Lingkungan Pesisir & Pelabuhan", "Spesialis Survei Hidro-Oseanografi Bawah Laut"],
            "en": ["Offshore Metocean Engineer in Energy Sector", "Marine & Tsunami Modeling Analyst", "Coastal Engineering & Port Consultant", "Hydro-Oceanographic Survey Specialist"]
        }
    },
    # FTSL Jatinangor
    {
        "id": "s1-teknik-dan-pengelolaan-sumber-daya-air",
        "kode": "15801",
        "nama": "Teknik dan Pengelolaan Sumber Daya Air",
        "nama_en": "Water Resources Engineering and Management",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTSL-J (Jatinangor)",
        "lokasi": "Kampus ITB Jatinangor (Sumedang)",
        "fakultas": "Fakultas Teknik Sipil dan Lingkungan", "fakultas_singkatan": "FTSL",
        "akreditasi": "Unggul", "akreditasi_skor": "374",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 24, "dt_smitb": 18,
        "website": "https://ftsl.itb.ac.id/tpsda",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Rekayasa hidrologi terpadu, desain bendungan dan waduk, pengendalian banjir wilayah sungai, serta tata kelola konservasi air tanah dan irigasi modern.",
            "en": "Integrated hydrological engineering, dam and reservoir design, watershed flood management, groundwater conservation, and modern irrigation infrastructure."
        },
        "fokus": {
            "id": ["Hidrologi Terapan & Pemodelan Aliran Sungai", "Desain Bangunan Air & Bendungan Waduk", "Pengendalian Banjir & Mitigasi Kekeringan", "Pengelolaan Terpadu Wilayah Sungai (IWRM)"],
            "en": ["Applied Hydrology & River Flow Modeling", "Hydraulic Structures & Dam Design", "Flood Control & Drought Mitigation", "Integrated Water Resources Management (IWRM)"]
        },
        "karir": {
            "id": ["Water Resources Engineer di Kementerian PUPR", "Hydraulic Modeler & Dam Safety Engineer", "Konsultan Konservasi DAS & Pengendalian Banjir", "Manager Pengelolaan Air Baku Perumda / Swasta"],
            "en": ["Water Resources Engineer at Ministry of Public Works", "Hydraulic Modeler & Dam Safety Specialist", "Watershed Conservation & Flood Management Consultant", "Raw Water Utility Manager"]
        }
    },
    # SITH Jatinangor
    {
        "id": "s1-teknologi-pasca-panen",
        "kode": "11901",
        "nama": "Teknologi Pasca Panen",
        "nama_en": "Post-Harvest Technology",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "SITH-R (Rekayasa)",
        "lokasi": "Kampus ITB Jatinangor (Sumedang)",
        "fakultas": "Sekolah Ilmu dan Teknologi Hayati", "fakultas_singkatan": "SITH",
        "akreditasi": "Unggul", "akreditasi_skor": "372",
        "akreditasi_internasional": ["ASIIN"],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 24, "dt_smitb": 18,
        "website": "https://sith.itb.ac.id/tpp",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Rekayasa rantai dingin logistik komoditas pertanian, teknologi pengemasan bioaktif, penurunan kehilangan hasil pascapanen, dan diversifikasi produk agroindustri.",
            "en": "Agricultural cold chain logistics engineering, bioactive packaging technology, post-harvest loss minimization, and value-added agro-industrial processing."
        },
        "fokus": {
            "id": ["Fisiologi Pascapanen Komoditas Pertanian", "Rekayasa Sistem Penyimpanan & Pendinginan", "Teknologi Pengemasan Cerdas & Pengawetan Alami", "Optimasi Rantai Pasok Agroindustri"],
            "en": ["Post-Harvest Physiology of Agricultural Produce", "Cold Chain & Storage Systems Engineering", "Smart Packaging & Natural Preservation Technology", "Agro-industrial Supply Chain Optimization"]
        },
        "karir": {
            "id": ["Post-Harvest Operations Lead di Korporasi Agribisnis", "Food Supply Chain & Cold Chain Logistics Manager", "Quality Assurance & Food Packaging Specialist", "Wirausahawan Teknologi Pengolahan Hasil Panen"],
            "en": ["Post-Harvest Operations Lead in Agribusiness", "Cold Chain Logistics & Supply Chain Manager", "Food Packaging & Quality Assurance Specialist", "Agro-processing Technology Entrepreneur"]
        }
    },
    # FSRD Ganesa (Seni Rupa & Kriya)
    {
        "id": "s1-seni-rupa",
        "kode": "17001",
        "nama": "Seni Rupa",
        "nama_en": "Fine Arts",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Seni & Desain",
        "tpb_fakultas": "FSRD-G (Ganesa)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Seni Rupa dan Desain", "fakultas_singkatan": "FSRD",
        "akreditasi": "Unggul", "akreditasi_skor": "378",
        "akreditasi_internasional": [],
        "daya_tampung": 60, "dt_snbp": 18, "dt_snbt": 24, "dt_smitb": 18,
        "website": "https://fsrd.itb.ac.id/senirupa",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Pengembangan karya seni lukis, patung, grafis, dan seni media baru kontemporer yang memadukan kepekaan estetika, diskursus kultural, dan eksplorasi material.",
            "en": "Creation of painting, sculpture, printmaking, and contemporary new media art blending aesthetic mastery, critical cultural discourse, and innovative materiality."
        },
        "fokus": {
            "id": ["Eksplorasi Seni Lukis & Patung Kontemporer", "Seni Grafis & Eksperimen Media Cetak", "Seni Instalasi & Media Interaktif", "Kritik Seni & Kurasi Galeri Pameran"],
            "en": ["Contemporary Painting & Sculptural Practices", "Printmaking & Print Media Innovation", "Installation Art & Interactive New Media", "Art Criticism & Gallery Exhibition Curating"]
        },
        "karir": {
            "id": ["Seniman Rupa Profesional Pameran Internasional", "Kurator Galeri Seni & Museum Nasional", "Art Director Galeri & Rumah Produksi Seni", "Pendidik & Kritikus Seni Rupa Kontemporer"],
            "en": ["Professional Fine Artist exhibiting globally", "Art Museum & Gallery Curator", "Fine Art Director & Studio Principal", "Art Critic & Contemporary Visual Arts Educator"]
        }
    },
    {
        "id": "s1-kriya",
        "kode": "17201",
        "nama": "Kriya",
        "nama_en": "Craft",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Seni & Desain",
        "tpb_fakultas": "FSRD-G (Ganesa)",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Fakultas Seni Rupa dan Desain", "fakultas_singkatan": "FSRD",
        "akreditasi": "Unggul", "akreditasi_skor": "376",
        "akreditasi_internasional": [],
        "daya_tampung": 50, "dt_snbp": 15, "dt_snbt": 20, "dt_smitb": 15,
        "website": "https://fsrd.itb.ac.id/kriya",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Transformasi kriya tekstil dan keramik kontemporer berbasis kekayaan kriya nusantara, teknologi material maju, serta nilai ekonomi kreatif bernilai tinggi.",
            "en": "Contemporary textile and ceramic craft innovation rooted in archipelago heritage, advanced material processing, and high-value creative economies."
        },
        "fokus": {
            "id": ["Eksplorasi Kriya Tekstil & Serat Alami", "Teknologi Kriya Keramik & Glasir Suhu Tinggi", "Desain Produk Kerajinan & Busana Etnik", "Manajemen Bisnis Kriya Berkelanjutan"],
            "en": ["Textile Craft & Natural Fiber Innovation", "Ceramic Craft & High-Fire Glaze Technology", "Craft Product & Sustainable Ethnic Fashion Design", "Artisanal Craft Enterprise Management"]
        },
        "karir": {
            "id": ["Kreator & Desainer Produk Kriya Mandiri (Artisan Entrepreneur)", "Desainer Tekstil & Serat di Industri Busana Global", "Studio Ceramic Designer & Kiln Master", "Konsultan Pengembangan Kerajinan Daerah & Warisan Budaya"],
            "en": ["Artisan Entrepreneur & Craft Designer", "Textile & Fiber Designer in Fashion Houses", "Studio Ceramic Designer & Ceramicist", "Craft Heritage Development Consultant"]
        }
    },
    # Kampus ITB Cirebon
    {
        "id": "s1-teknik-industri-cirebon",
        "kode": "13402",
        "nama": "Teknik Industri (Kampus Cirebon)",
        "nama_en": "Industrial Engineering (Cirebon Campus)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTI-C (Cirebon)",
        "lokasi": "Kampus ITB Cirebon",
        "fakultas": "Fakultas Teknologi Industri", "fakultas_singkatan": "FTI",
        "akreditasi": "Unggul", "akreditasi_skor": "375",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 50, "dt_snbp": 15, "dt_snbt": 20, "dt_smitb": 15,
        "website": "https://cirebon.itb.ac.id/ti",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Desain, optimasi, dan integrasi sistem manufaktur dan logistik berbasis wilayah kawasan industri pantura dan koridor Rebana Metropolitan.",
            "en": "Design, optimization, and integration of manufacturing and logistics systems tailored to the northern Java industrial and Rebana Metropolitan corridors."
        },
        "fokus": {
            "id": ["Optimasi Sistem Manufaktur Pantura", "Logistik Pelabuhan Patimban & Rantai Pasok", "Ergonomi & Produktivitas Kerja Industri", "Kajian Kelayakan & Tata Letak Pabrik Modern"],
            "en": ["Industrial Manufacturing Optimization", "Port Logistics & Supply Chain Systems", "Occupational Ergonomics & Plant Productivity", "Factory Layout & Feasibility Engineering"]
        },
        "karir": {
            "id": ["Operations Lead Kawasan Industri Rebana", "Supply Chain & Logistics Specialist di Korporasi Multinasional", "Plant Layout & Quality Engineering Manager", "Industrial Management Consultant"],
            "en": ["Rebana Industrial Zone Operations Lead", "Supply Chain & Logistics Specialist", "Plant Layout & Quality Engineering Manager", "Industrial Management Consultant"]
        }
    },
    {
        "id": "s1-perencanaan-wilayah-dan-kota-cirebon",
        "kode": "15402",
        "nama": "Perencanaan Wilayah dan Kota (Kampus Cirebon)",
        "nama_en": "Urban and Regional Planning (Cirebon Campus)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "SAPPK-C (Cirebon)",
        "lokasi": "Kampus ITB Cirebon",
        "fakultas": "Sekolah Arsitektur, Perencanaan dan Pengembangan Kebijakan", "fakultas_singkatan": "SAPPK",
        "akreditasi": "Unggul", "akreditasi_skor": "374",
        "akreditasi_internasional": [],
        "daya_tampung": 50, "dt_snbp": 15, "dt_snbt": 20, "dt_smitb": 15,
        "website": "https://cirebon.itb.ac.id/pwk",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Perencanaan tata ruang wilayah maritim pesisir, pengembangan kota pelabuhan transit, ketahanan iklim pantura, dan konektivitas infrastruktur trans-Jawa.",
            "en": "Coastal spatial planning, maritime port-city development, northern Java climate resilience, and trans-Java connectivity infrastructure planning."
        },
        "fokus": {
            "id": ["Perencanaan Tata Ruang Kota Maritim & Pesisir", "Pengembangan Kawasan Industri & Aerotropolis Kertajati", "Manajemen Infrastruktur & Transportasi Pantura", "Sistem Informasi Spasial Perencanaan Kota"],
            "en": ["Maritime & Coastal Spatial Planning", "Aerotropolis & Industrial Zone Development", "Pantura Transportation Infrastructure Planning", "Geospatial Urban Analytics"]
        },
        "karir": {
            "id": ["Perencana Kota & Wilayah di Bappeda / Kementerian ATR-BPN", "Urban Planner Masterplan Kawasan Strategis Terpadu", "Spesialis Transportasi & Logistik Wilayah", "Konsultan Tata Ruang Wilayah Pesisir"],
            "en": ["Urban & Regional Planner at Bappeda/ATR-BPN", "Masterplan Urban Development Lead", "Regional Transportation & Infrastructure Specialist", "Coastal Spatial Planning Consultant"]
        }
    },
    {
        "id": "s1-kriya-cirebon",
        "kode": "17202",
        "nama": "Kriya (Kampus Cirebon)",
        "nama_en": "Craft (Cirebon Campus)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Seni & Desain",
        "tpb_fakultas": "FSRD-C (Cirebon)",
        "lokasi": "Kampus ITB Cirebon",
        "fakultas": "Fakultas Seni Rupa dan Desain", "fakultas_singkatan": "FSRD",
        "akreditasi": "Unggul", "akreditasi_skor": "372",
        "akreditasi_internasional": [],
        "daya_tampung": 40, "dt_snbp": 12, "dt_snbt": 16, "dt_smitb": 12,
        "website": "https://cirebon.itb.ac.id/kriya",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Revitalisasi kriya batik pesisiran (Mega Mendung), kriya rotan Cirebon berdaya saing global, keramik lokal, dan pengembangan produk interior kerajinan ekspor.",
            "en": "Revitalization of coastal batik heritage (Mega Mendung), global-standard Cirebon rattan craft, regional ceramics, and export-grade interior crafts."
        },
        "fokus": {
            "id": ["Inovasi Desain Kriya Rotan & Furnitur Modern", "Kriya Batik Pesisir & Pewarnaan Alami Berkelanjutan", "Keramik Dekoratif & Peralatan Rumah Tangga", "Branding & Pemasaran Global Produk Kriya"],
            "en": ["Modern Rattan Craft & Furniture Innovation", "Coastal Batik & Sustainable Natural Dyeing", "Decorative Ceramics & Tableware Design", "Global Craft Branding & Export Strategy"]
        },
        "karir": {
            "id": ["Desainer Furnitur & Kriya Rotan Ekspor", "Pengusaha Kerajinan Kreatif & Batik Nusantara", "Creative Director Perusahaan Dekorasi Interior", "Konsultan Desain Produk Kerajinan Berkelanjutan"],
            "en": ["Export-Grade Rattan & Furniture Designer", "Artisan Craft & Batik Brand Founder", "Interior Home Decor Creative Director", "Sustainable Craft Product Consultant"]
        }
    },
    {
        "id": "s1-teknik-perminyakan-cirebon",
        "kode": "12202",
        "nama": "Teknik Perminyakan (Kampus Cirebon)",
        "nama_en": "Petroleum Engineering (Cirebon Campus)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTTM-C (Cirebon)",
        "lokasi": "Kampus ITB Cirebon",
        "fakultas": "Fakultas Teknik Pertambangan dan Perminyakan", "fakultas_singkatan": "FTTM",
        "akreditasi": "Unggul", "akreditasi_skor": "376",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 50, "dt_snbp": 15, "dt_snbt": 20, "dt_smitb": 15,
        "website": "https://cirebon.itb.ac.id/tm",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Eksploitasi reservoir hidrokarbon, pengeboran sumur migas, enhanced oil recovery (EOR), dan penangkapan karbon (CCS/CCUS) di cekungan migas Jawa Barat.",
            "en": "Hydrocarbon reservoir exploitation, drilling engineering, enhanced oil recovery (EOR), and carbon capture storage (CCS/CCUS) in West Java basins."
        },
        "fokus": {
            "id": ["Teknik Reservoir & Karakterisasi Batuan Poros", "Teknik Pengeboran Canggih & Well Integrity", "Teknik Produksi & Pengolahan Fasilitas Permukaan", "Enhanced Oil Recovery & Karbon Storage (CCUS)"],
            "en": ["Reservoir Engineering & Porous Media Characterization", "Advanced Drilling Engineering & Well Integrity", "Production Engineering & Surface Facilities", "Enhanced Oil Recovery & CCUS Technologies"]
        },
        "karir": {
            "id": ["Petroleum Reservoir Engineer di Korporasi Migas", "Drilling Engineer Lapangan Lepas Pantai & Onshore", "Production Technologist Fasilitas Hulu Migas", "Energy Transition & Geothermal Well Specialist"],
            "en": ["Petroleum Reservoir Engineer", "Drilling & Completions Engineer", "Upstream Production Technologist", "Energy Transition & Geothermal Specialist"]
        }
    },
    {
        "id": "s1-teknik-pertambangan-cirebon",
        "kode": "12102",
        "nama": "Teknik Pertambangan (Kampus Cirebon)",
        "nama_en": "Mining Engineering (Cirebon Campus)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTTM-C (Cirebon)",
        "lokasi": "Kampus ITB Cirebon",
        "fakultas": "Fakultas Teknik Pertambangan dan Perminyakan", "fakultas_singkatan": "FTTM",
        "akreditasi": "Unggul", "akreditasi_skor": "375",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 50, "dt_snbp": 15, "dt_snbt": 20, "dt_smitb": 15,
        "website": "https://cirebon.itb.ac.id/ta",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Perencanaan tambang terbuka dan tambang bawah tanah, geomekanika batuan, keselamatan pertambangan (K3), serta reklamasi lahan pascatambang berwawasan lingkungan.",
            "en": "Open-pit and underground mine planning, rock geomechanics, mining health and safety (OHS), and sustainable post-mining land reclamation."
        },
        "fokus": {
            "id": ["Perencanaan & Penjadwalan Tambang Berkelanjutan", "Geomekanika Batuan & Kestabilan Lereng", "Teknik Peledakan Presisi & Ventilasi Tambang", "Reklamasi Lingkungan & Penutupan Tambang"],
            "en": ["Sustainable Mine Planning & Fleet Optimization", "Rock Geomechanics & Slope Stability", "Precision Blasting & Underground Ventilation", "Mine Environmental Rehabilitation"]
        },
        "karir": {
            "id": ["Mine Planning Engineer di Industri Pertambangan Terkemuka", "Geotechnical Engineer Lereng Tambang Terbuka", "Operational Mine Safety Superintendent", "Konsultan Valuasi Properti Tambang & AMDAL"],
            "en": ["Mine Planning Engineer in Global Mining", "Mine Geotechnical Stability Engineer", "Mining Operational Safety Superintendent", "Mine Valuation & Reclamation Consultant"]
        }
    },
    {
        "id": "s1-teknik-geofisika-cirebon",
        "kode": "12302",
        "nama": "Teknik Geofisika (Kampus Cirebon)",
        "nama_en": "Geophysical Engineering (Cirebon Campus)",
        "jenjang": "S1", "kategori": "Sarjana", "rumpun": "Saintek",
        "tpb_fakultas": "FTTM-C (Cirebon)",
        "lokasi": "Kampus ITB Cirebon",
        "fakultas": "Fakultas Teknik Pertambangan dan Perminyakan", "fakultas_singkatan": "FTTM",
        "akreditasi": "Unggul", "akreditasi_skor": "374",
        "akreditasi_internasional": ["IABEE"],
        "daya_tampung": 50, "dt_snbp": 15, "dt_snbt": 20, "dt_smitb": 15,
        "website": "https://cirebon.itb.ac.id/tg",
        "ukt_rentang": "UKT 1 (Rp 0) s/d UKT 5 (Rp 12.500.000)",
        "deskripsi": {
            "id": "Aplikasi metode fisika bumi (seismik, gravitasi, magnetik, geolistrik) untuk eksplorasi energi panas bumi, air tanah dalam, dan investigasi geoteknik pantura.",
            "en": "Application of geophysical methods (seismic, gravity, magnetic, electrical) for geothermal exploration, deep groundwater mapping, and geotechnical investigations."
        },
        "fokus": {
            "id": ["Eksplorasi Seismik Refleksi & Tomografi", "Metode Elektromagnetik & Geolistrik Tahanan Jenis", "Eksplorasi Energi Panas Bumi (Geotermal)", "Geofisika Dekat Permukaan & Mitigasi Gempa"],
            "en": ["Seismic Reflection & Traveltime Tomography", "Electromagnetic & Electrical Resistivity Methods", "Geothermal Energy Reservoir Exploration", "Near-Surface Geophysics & Earthquake Hazards"]
        },
        "karir": {
            "id": ["Exploration Geophysicist di Industri Geotermal & Migas", "Seismic Data Processing & Inversion Specialist", "Near-Surface Geophysical Surveyor Konstruksi", "Analis Bahaya Seismik & Kebumian BMKG"],
            "en": ["Exploration Geophysicist in Geothermal/Energy", "Seismic Processing & Inversion Specialist", "Near-Surface Geotechnical Geophysicist", "Seismic Hazard Analyst at Geological Agencies"]
        }
    },
    # =========================================================================
    # 12. PROGRAM PASCASARJANA MULTIDISIPLIN (SPS / Multi-Fakultas)
    # =========================================================================
    {
        "id": "s2-studi-pembangunan",
        "kode": "24001",
        "nama": "Studi Pembangunan",
        "nama_en": "Development Studies",
        "jenjang": "S2", "kategori": "Magister", "rumpun": "Soshum",
        "tpb_fakultas": "SAPPK",
        "lokasi": "Kampus ITB Ganesa (Bandung)",
        "fakultas": "Sekolah Arsitektur, Perencanaan dan Pengembangan Kebijakan", "fakultas_singkatan": "SAPPK",
        "akreditasi": "Unggul", "akreditasi_skor": "378",
        "akreditasi_internasional": [],
        "daya_tampung": 40, "dt_snbp": 0, "dt_snbt": 0, "dt_smitb": 40,
        "website": "https://sappk.itb.ac.id",
        "ukt_rentang": "Rp 15.000.000 per semester",
        "deskripsi": {
            "id": "Analisis kebijakan ekonomi politik pembangunan, keadilan sosial spasial, pengentasan kemiskinan, dan tata kelola sumber daya alam berkelanjutan.",
            "en": "Analyzes political economy of development, spatial equity, poverty alleviation, and sustainable governance of natural capital."
        },
        "fokus": {
            "id": ["Teori & Kebijakan Pembangunan Berkelanjutan", "Ekonomi Politik Pembangunan & Kemiskinan", "Pemberdayaan Masyarakat & Transformasi Sosial", "Evaluasi Kebijakan Publik Nasional"],
            "en": ["Sustainable Development Policy", "Political Economy of Development", "Community Empowerment & Social Change", "Public Policy Impact Evaluation"]
        },
        "karir": {
            "id": ["Development Policy Analyst di Bappenas / Bank Dunia", "Program Officer di Lembaga PBB (UNDP/UNICEF)", "Social Impact & ESG Consultant", "Peneliti Kebijakan Publik"],
            "en": ["Development Policy Analyst (World Bank/Bappenas)", "UN Agency Program Officer", "Social Impact & ESG Lead", "Think Tank Policy Researcher"]
        }
    },
    {
        "id": "s2-magister-bisnis-administrasi",
        "kode": "29001",
        "nama": "Magister Bisnis Administrasi",
        "nama_en": "Master of Business Administration (MBA ITB)",
        "jenjang": "S2", "kategori": "Magister", "rumpun": "Bisnis & Manajemen",
        "tpb_fakultas": "SBM",
        "lokasi": "Kampus ITB Ganesa & Jakarta",
        "fakultas": "Sekolah Bisnis dan Manajemen", "fakultas_singkatan": "SBM",
        "akreditasi": "Unggul", "akreditasi_skor": "386",
        "akreditasi_internasional": ["AACSB"],
        "daya_tampung": 200, "dt_snbp": 0, "dt_snbt": 0, "dt_smitb": 200,
        "website": "https://sbm.itb.ac.id/mba",
        "ukt_rentang": "Rp 25.000.000 - Rp 38.000.000 per semester",
        "deskripsi": {
            "id": "Program MBA berperingkat internasional AACSB, mencetak eksekutif puncak dan pemimpin bisnis dengan kurikulum kepemimpinan strategis, private equity, dan inovasi disruptif.",
            "en": "AACSB-accredited elite MBA program cultivating C-suite executives in strategic leadership, private equity valuation, and digital enterprise transformation."
        },
        "fokus": {
            "id": ["Executive Strategic Decision Making", "Corporate Valuation & Mergers Acquisitions", "Disruptive Innovation & Business Scaling", "Sustainability Leadership & ESG Strategy"],
            "en": ["Executive Strategic Decision Making", "Corporate Valuation & Mergers Acquisitions", "Disruptive Innovation & Business Scaling", "Sustainability Leadership & ESG Strategy"]
        },
        "karir": {
            "id": ["Chief Executive Officer (CEO) / C-Level Executive", "Managing Director Private Equity / Venture Capital", "Senior Strategy Partner di Firma Konsultan", "VP of Business Development & Expansion"],
            "en": ["C-Suite Corporate Executive", "Managing Director in Private Equity / VC", "Senior Management Consulting Partner", "Vice President of Business Development"]
        }
    }
]

def generate_datasets():
    print(f"Generating ITB study program dataset... Total programs: {len(RAW_PRODI)}")
    
    # 1. Write JSON
    json_path = os.path.join(DATA_DIR, "itb_prodi.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(RAW_PRODI, f, indent=2, ensure_ascii=False)
    print(f"Written: {json_path}")

    # 2. Extract faculties metadata
    faculties_map = {}
    for p in RAW_PRODI:
        f_code = p["fakultas_singkatan"]
        if f_code not in faculties_map:
            faculties_map[f_code] = {
                "singkatan": f_code,
                "nama": p["fakultas"],
                "lokasi": p["lokasi"]
            }

    # 3. Write JS (for static web consumption)
    js_path = os.path.join(DATA_DIR, "itb_prodi.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("// Dataset Resmi Direktori Program Studi Institut Teknologi Bandung (ITB)\n")
        f.write(f"// Diperbarui: {datetime.date.today().strftime('%d %B %Y')}\n\n")
        f.write("window.ITB_METADATA = " + json.dumps(ITB_METADATA, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("window.ITB_FACULTIES = " + json.dumps(faculties_map, indent=2, ensure_ascii=False) + ";\n\n")
        f.write("window.ITB_PRODI_DATA = " + json.dumps(RAW_PRODI, indent=2, ensure_ascii=False) + ";\n")
    print(f"Written: {js_path}")

    # 4. Write CSV
    csv_path = os.path.join(DATA_DIR, "itb_prodi.csv")
    csv_fields = [
        "id", "kode", "nama", "nama_en", "jenjang", "kategori", "rumpun",
        "tpb_fakultas", "fakultas", "fakultas_singkatan", "lokasi", "akreditasi",
        "akreditasi_skor", "akreditasi_internasional", "daya_tampung", "dt_snbp",
        "dt_snbt", "dt_smitb", "website", "ukt_rentang"
    ]
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for p in RAW_PRODI:
            row = {
                "id": p["id"],
                "kode": p["kode"],
                "nama": p["nama"],
                "nama_en": p["nama_en"],
                "jenjang": p["jenjang"],
                "kategori": p["kategori"],
                "rumpun": p["rumpun"],
                "tpb_fakultas": p["tpb_fakultas"],
                "fakultas": p["fakultas"],
                "fakultas_singkatan": p["fakultas_singkatan"],
                "lokasi": p["lokasi"],
                "akreditasi": p["akreditasi"],
                "akreditasi_skor": p["akreditasi_skor"],
                "akreditasi_internasional": "; ".join(p["akreditasi_internasional"]),
                "daya_tampung": p["daya_tampung"],
                "dt_snbp": p["dt_snbp"],
                "dt_snbt": p["dt_snbt"],
                "dt_smitb": p["dt_smitb"],
                "website": p["website"],
                "ukt_rentang": p["ukt_rentang"]
            }
            writer.writerow(row)
    print(f"Written: {csv_path}")

    # 5. Write metadata.json
    now = datetime.datetime.now()
    metadata_path = os.path.join(DATA_DIR, "metadata.json")
    meta_content = {
        "title": "Institut Teknologi Bandung Study Programs & Accreditation Directory",
        "university": "Institut Teknologi Bandung",
        "acronym": "ITB",
        "last_updated_iso": now.isoformat(),
        "last_updated_date": now.strftime("%d %B %Y"),
        "total_prodi": len(RAW_PRODI),
        "total_fakultas": len(faculties_map),
        "total_s1": sum(1 for p in RAW_PRODI if p["jenjang"] == "S1"),
        "total_pascasarjana": sum(1 for p in RAW_PRODI if p["jenjang"] in ("S2", "S3")),
        "total_unggul": sum(1 for p in RAW_PRODI if p["akreditasi"] == "Unggul"),
        "total_akreditasi_internasional": sum(1 for p in RAW_PRODI if len(p["akreditasi_internasional"]) > 0),
        "source": "https://admission.itb.ac.id",
        "license": "MIT"
    }
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(meta_content, f, indent=2, ensure_ascii=False)
    print(f"Written: {metadata_path}")
    print("Dataset generation completed successfully.")

if __name__ == "__main__":
    generate_datasets()
