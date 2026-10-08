<template>
  <div class="layout-container">
    <!-- Bočna navigacija / Izbornik -->
    <aside class="sidebar">
      <div class="brand">
        <div class="brand-icon">🏨</div>
        <div>
          <h2>Recepcija360</h2>
          <p>PMS Manager</p>
        </div>
      </div>

      <nav class="nav-menu">
        <button class="nav-btn active">
          <span>📊</span> Pregled Soba
        </button>
      </nav>

      <div class="system-status">
        <span class="status-dot"></span>
        Sistem aktivan • Web Cloud
      </div>
    </aside>

    <!-- Glavni sadržaj -->
    <main class="main-content">
      <header class="content-header">
        <div>
          <h1>Pregled Soba</h1>
          <p class="date-subtitle">{{ trenutniDatum }}</p>
        </div>
      </header>

      <!-- Statističke kartice -->
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-icon slobodno">🟢</div>
          <div>
            <div class="stat-label">SLOBODNO</div>
            <div class="stat-value">{{ slobodneSobeCount }}</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon zauzeto">🔴</div>
          <div>
            <div class="stat-label">ZAUZETO</div>
            <div class="stat-value">{{ zauzeteSobeCount }}</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon odlazak">🚪</div>
          <div>
            <div class="stat-label">ČIŠĆENJE</div>
            <div class="stat-value">{{ ciscenjeSobeCount }}</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon popunjenost">📈</div>
          <div>
            <div class="stat-label">POPUNJENOST</div>
            <div class="stat-value">{{ popunjenostPostotak }}%</div>
          </div>
        </div>
      </div>

      <!-- Filteri: Status, Kategorija, Tip Kreveta i Bide -->
      <div class="filter-section">
        <div class="filter-row">
          <span class="filter-label">STATUS:</span>
          <button :class="{ active: odabraniStatus === 'svi' }" @click="postaviFilter('status', 'svi')" class="filter-chip">Sve Sobe</button>
          <button :class="{ active: odabraniStatus === 'Slobodna' }" @click="postaviFilter('status', 'Slobodna')" class="filter-chip">Slobodne (Zeleno)</button>
          <button :class="{ active: odabraniStatus === 'Zauzeta' }" @click="postaviFilter('status', 'Zauzeta')" class="filter-chip">Zauzete (Crveno)</button>
          <button :class="{ active: odabraniStatus === 'Čišćenje' }" @click="postaviFilter('status', 'Čišćenje')" class="filter-chip">Čišćenje (Žuto)</button>
        </div>

        <div class="filter-row" style="margin-top: 10px;">
          <span class="filter-label">KATEGORIJA:</span>
          <button :class="{ active: odabranaKategorija === 'sve' }" @click="postaviFilter('kategorija', 'sve')" class="filter-chip">Sve</button>
          <button :class="{ active: odabranaKategorija === 'Stara soba' }" @click="postaviFilter('kategorija', 'Stara soba')" class="filter-chip">Stara soba</button>
          <button :class="{ active: odabranaKategorija === 'Nova soba' }" @click="postaviFilter('kategorija', 'Nova soba')" class="filter-chip">Nova soba</button>

          <span class="filter-label" style="margin-left: 15px;">KREVETI:</span>
          <button :class="{ active: odabraniKrevet === 'svi' }" @click="postaviFilter('krevet', 'svi')" class="filter-chip">Svi kreveti</button>
          <button :class="{ active: odabraniKrevet === 'Odvojeni kreveti' }" @click="postaviFilter('krevet', 'Odvojeni kreveti')" class="filter-chip">Odvojeni kreveti</button>
          <button :class="{ active: odabraniKrevet === 'Bračni krevet' }" @click="postaviFilter('krevet', 'Bračni krevet')" class="filter-chip">Bračni krevet</button>
          <button :class="{ active: odabraniKrevet === 'Bračna odvojiva' }" @click="postaviFilter('krevet', 'Bračna odvojiva')" class="filter-chip">Bračna odvojiva</button>
        </div>

        <div class="filter-row" style="margin-top: 10px;">
          <span class="filter-label">BIDE:</span>
          <button :class="{ active: odabraniBide === 'svi' }" @click="postaviFilter('bide', 'svi')" class="filter-chip">Sve sobe</button>
          <button :class="{ active: odabraniBide === 'da' }" @click="postaviFilter('bide', 'da')" class="filter-chip">S bideom 🚽</button>
          <button :class="{ active: odabraniBide === 'ne' }" @click="postaviFilter('bide', 'ne')" class="filter-chip">Bez bidea</button>
        </div>
      </div>

      <!-- GRUPA: STARA SOBA -->
      <div class="sprat-group" v-if="odabranaKategorija === 'sve' || odabranaKategorija === 'Stara soba'">
        <h3 class="sprat-title">🏢 Stara soba <span>({{ stareSobeFiltrirane.length }} soba)</span></h3>
        
        <div class="sobe-grid" v-if="stareSobeFiltrirane.length > 0">
          <div 
            v-for="soba in stareSobeFiltrirane" 
            :key="soba.id || soba.broj_sobe" 
            class="soba-card"
            :class="dohvatiKlasuStatusa(soba.status)"
          >
            <div class="card-top">
              <span class="tip-label">
                {{ soba.tip_kreveta || 'Standard' }}
                <span v-if="provjeriBide(soba)" class="bide-tag">| 🚽 Bide</span>
              </span>
              <span class="status-pill" :class="dohvatiKlasuStatusa(soba.status)">
                ● {{ soba.status || 'Slobodna' }}
              </span>
            </div>

            <div class="soba-header-row">
              <h2 class="soba-broj">Soba {{ soba.broj_sobe }}</h2>
              <span class="kapacitet-badge" v-if="soba.kapacitet || soba.broj_kreveta">
                👤 {{ soba.kapacitet || soba.broj_kreveta }}
              </span>
            </div>
            
            <p class="gost-info">{{ soba.kategorija || 'Stara soba' }}</p>

            <div class="card-action-btn">
              <select 
                class="status-select" 
                :class="dohvatiKlasuStatusa(soba.status)"
                :value="soba.status || 'Slobodna'" 
                @change="promijeniStatus(soba, $event.target.value)"
              >
                <option value="Slobodna">🟢 Slobodna</option>
                <option value="Zauzeta">🔴 Zauzeta</option>
                <option value="Čišćenje">🟡 Čišćenje</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      <!-- GRUPA: NOVA SOBA -->
      <div class="sprat-group" v-if="odabranaKategorija === 'sve' || odabranaKategorija === 'Nova soba'">
        <h3 class="sprat-title">🏢 Nova soba <span>({{ noveSobeFiltrirane.length }} soba)</span></h3>
        
        <div class="sobe-grid" v-if="noveSobeFiltrirane.length > 0">
          <div 
            v-for="soba in noveSobeFiltrirane" 
            :key="soba.id || soba.broj_sobe" 
            class="soba-card"
            :class="dohvatiKlasuStatusa(soba.status)"
          >
            <div class="card-top">
              <span class="tip-label">
                {{ soba.tip_kreveta || 'Standard' }}
                <span v-if="provjeriBide(soba)" class="bide-tag">| 🚽 Bide</span>
              </span>
              <span class="status-pill" :class="dohvatiKlasuStatusa(soba.status)">
                ● {{ soba.status || 'Slobodna' }}
              </span>
            </div>

            <div class="soba-header-row">
              <h2 class="soba-broj">Soba {{ soba.broj_sobe }}</h2>
              <span class="kapacitet-badge" v-if="soba.kapacitet || soba.broj_kreveta">
                👤 {{ soba.kapacitet || soba.broj_kreveta }}
              </span>
            </div>
            
            <p class="gost-info">{{ soba.kategorija || 'Nova soba' }}</p>

            <div class="card-action-btn">
              <select 
                class="status-select" 
                :class="dohvatiKlasuStatusa(soba.status)"
                :value="soba.status || 'Slobodna'" 
                @change="promijeniStatus(soba, $event.target.value)"
              >
                <option value="Slobodna">🟢 Slobodna</option>
                <option value="Zauzeta">🔴 Zauzeta</option>
                <option value="Čišćenje">🟡 Čišćenje</option>
              </select>
            </div>
          </div>
        </div>
      </div>

    </main>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000';

export default {
  data() {
    return {
      sobe: [],
      // Učitavanje zatečenih/zapamćenih filtera iz localStorage
      odabraniStatus: localStorage.getItem('f_status') || 'svi',
      odabranaKategorija: localStorage.getItem('f_kategorija') || 'sve',
      odabraniKrevet: localStorage.getItem('f_krevet') || 'svi',
      odabraniBide: localStorage.getItem('f_bide') || 'svi',
      trenutniDatum: new Date().toLocaleDateString('hr-HR', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
    };
  },
  computed: {
    filtriraneSobe() {
      return this.sobe.filter(soba => {
        // 1. STATUS FILTER
        const st = (soba.status || 'Slobodna').toLowerCase();
        let pasujeStatus = true;
        if (this.odabraniStatus !== 'svi') {
          const trazeniStatus = this.odabraniStatus.toLowerCase();
          pasujeStatus = st.includes(trazeniStatus) || (trazeniStatus.includes('čišć') && st.includes('čišć'));
        }

        // 2. KATEGORIJA FILTER
        const kat = (soba.kategorija || '').toLowerCase();
        let pasujeKategorija = true;
        if (this.odabranaKategorija === 'Stara soba') {
          pasujeKategorija = kat.includes('star');
        } else if (this.odabranaKategorija === 'Nova soba') {
          pasujeKategorija = kat.includes('nov');
        }

        // 3. TIP KREVETA FILTER
        const tip = (soba.tip_kreveta || '').toLowerCase();
        let pasujeKrevet = true;
        if (this.odabraniKrevet === 'Odvojeni kreveti') {
          pasujeKrevet = tip.includes('odvoj') || tip.includes('spoj') || tip.includes('2x1') || tip.includes('jednokrevet');
        } else if (this.odabraniKrevet === 'Bračni krevet') {
          pasujeKrevet = (tip.includes('brač') || tip.includes('brac') || tip.includes('double')) && !tip.includes('odvojiv');
        } else if (this.odabraniKrevet === 'Bračna odvojiva') {
          pasujeKrevet = tip.includes('odvojiv') || (tip.includes('brač') && tip.includes('odvoj'));
        }

        // 4. BIDE FILTER
        const imaBide = this.provjeriBide(soba);
        let pasujeBide = true;
        if (this.odabraniBide === 'da') {
          pasujeBide = imaBide === true;
        } else if (this.odabraniBide === 'ne') {
          pasujeBide = imaBide === false;
        }

        return pasujeStatus && pasujeKategorija && pasujeKrevet && pasujeBide;
      });
    },

    stareSobeFiltrirane() {
      return this.filtriraneSobe.filter(s => {
        const kat = (s.kategorija || '').toLowerCase();
        return kat.includes('star') || (!kat.includes('nov') && (s.broj_sobe < 200 || String(s.broj_sobe).startsWith('1')));
      });
    },

    noveSobeFiltrirane() {
      return this.filtriraneSobe.filter(s => {
        const kat = (s.kategorija || '').toLowerCase();
        return kat.includes('nov') || (!kat.includes('star') && (s.broj_sobe >= 200 || String(s.broj_sobe).startsWith('2')));
      });
    },

    slobodneSobeCount() {
      return this.sobe.filter(s => (s.status || 'Slobodna').toLowerCase() === 'slobodna').length;
    },
    zauzeteSobeCount() {
      return this.sobe.filter(s => (s.status || '').toLowerCase() === 'zauzeta').length;
    },
    ciscenjeSobeCount() {
      return this.sobe.filter(s => {
        const st = (s.status || '').toLowerCase();
        return st.includes('čišć') || st.includes('cisc');
      }).length;
    },
    popunjenostPostotak() {
      if (!this.sobe.length) return 0;
      return Math.round((this.zauzeteSobeCount / this.sobe.length) * 100);
    }
  },
  mounted() {
    this.dohvatiSobe();
  },
  methods: {
    postaviFilter(tip, vrijednost) {
      if (tip === 'status') {
        this.odabraniStatus = vrijednost;
        localStorage.setItem('f_status', vrijednost);
      } else if (tip === 'kategorija') {
        this.odabranaKategorija = vrijednost;
        localStorage.setItem('f_kategorija', vrijednost);
      } else if (tip === 'krevet') {
        this.odabraniKrevet = vrijednost;
        localStorage.setItem('f_krevet', vrijednost);
      } else if (tip === 'bide') {
        this.odabraniBide = vrijednost;
        localStorage.setItem('f_bide', vrijednost);
      }
    },

    provjeriBide(soba) {
      if (!soba) return false;
      return Boolean(
        soba.ima_bide === true || 
        soba.bide === true || 
        soba.ima_bide === 1 || 
        soba.bide === 1 || 
        String(soba.ima_bide).toLowerCase() === 'da' ||
        String(soba.bide).toLowerCase() === 'da'
      );
    },

    dohvatiKlasuStatusa(status) {
      const st = (status || 'slobodna').toLowerCase();
      if (st.includes('zauzet')) return 'zauzeta';
      if (st.includes('čišć') || st.includes('cisc')) return 'čišćenje';
      return 'slobodna';
    },

    async dohvatiSobe() {
      try {
        const res = await axios.get(`${API_URL}/api/sobe`);
        
        // Sačuvaj lokalne izmjene statusa iz localStorage ako API nije uspio ažurirati backend
        const lokalniStatusi = JSON.parse(localStorage.getItem('lokalni_statusi_soba') || '{}');

        this.sobe = res.data.map(soba => {
          if (lokalniStatusi[soba.id || soba.broj_sobe]) {
            soba.status = lokalniStatusi[soba.id || soba.broj_sobe];
          }
          return soba;
        });
      } catch (err) {
        console.error('Greška pri dohvatanju soba:', err);
      }
    },

    async promijeniStatus(soba, noviStatus) {
      const sobaId = soba.id || soba.broj_sobe;
      
      // 1. Odmah ažuriraj vizualno i zapamti lokalno da ne nestane pri refresh-u
      soba.status = noviStatus;
      const lokalniStatusi = JSON.parse(localStorage.getItem('lokalni_statusi_soba') || '{}');
      lokalniStatusi[sobaId] = noviStatus;
      localStorage.setItem('lokalni_statusi_soba', JSON.stringify(lokalniStatusi));

      // 2. Pošalji na server
      try {
        await axios.patch(`${API_URL}/api/sobe/${sobaId}/status`, { status: noviStatus });
      } catch (err) {
        console.warn('Backend patch nije uspio, spremljeno lokalno u pregledniku:', err);
      }
    }
  }
};
</script>

<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background-color: #f8fafc; color: #1e293b; overflow-x: hidden; }

.layout-container { display: flex; min-height: 100vh; width: 100%; }

/* Sidebar za desktop */
.sidebar { 
  width: 240px; 
  min-width: 240px; 
  background: #0f172a; 
  color: white; 
  padding: 24px 16px; 
  display: flex; 
  flex-direction: column; 
  flex-shrink: 0; 
}
.brand { display: flex; align-items: center; gap: 12px; margin-bottom: 32px; }
.brand-icon { font-size: 28px; background: #1e293b; padding: 8px; border-radius: 12px; }
.brand h2 { font-size: 18px; font-weight: 700; }
.brand p { font-size: 11px; color: #94a3b8; }

.nav-menu { display: flex; flex-direction: column; gap: 8px; flex-grow: 1; }
.nav-btn { display: flex; align-items: center; gap: 12px; padding: 12px 16px; border: none; background: transparent; color: #94a3b8; border-radius: 8px; font-weight: 600; cursor: pointer; text-align: left; }
.nav-btn.active { background: #2563eb; color: white; }

.system-status { font-size: 12px; color: #64748b; display: flex; align-items: center; gap: 8px; margin-top: auto; }
.status-dot { width: 8px; height: 8px; background: #10b981; border-radius: 50%; }

/* Main Content */
.main-content { flex: 1; padding: 32px; min-width: 0; overflow-y: auto; }
.date-subtitle { color: #64748b; font-size: 14px; margin-top: 4px; }

/* Stats */
.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin: 24px 0; }
.stat-card { background: white; padding: 20px; border-radius: 14px; display: flex; align-items: center; gap: 16px; border: 1px solid #e2e8f0; }
.stat-icon { font-size: 24px; padding: 12px; border-radius: 12px; }
.stat-icon.slobodno { background: #dcfce7; }
.stat-icon.zauzeto { background: #fee2e2; }
.stat-icon.odlazak { background: #fef3c7; }
.stat-icon.popunjenost { background: #dbeafe; }
.stat-label { font-size: 11px; font-weight: 700; color: #64748b; letter-spacing: 0.5px; }
.stat-value { font-size: 24px; font-weight: 800; color: #0f172a; margin-top: 2px; }

/* Filters */
.filter-section { background: white; padding: 16px; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 28px; }
.filter-row { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.filter-label { font-size: 11px; font-weight: 800; color: #94a3b8; min-width: 80px; }
.filter-chip { padding: 6px 12px; border-radius: 8px; border: 1px solid #cbd5e1; background: #f8fafc; cursor: pointer; font-weight: 600; color: #475569; font-size: 13px; }
.filter-chip.active { background: #0f172a; color: white; border-color: #0f172a; }

/* Grupiranje po kategorijama */
.sprat-group { margin-bottom: 32px; }
.sprat-title { font-size: 16px; font-weight: 800; color: #0f172a; margin-bottom: 16px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }
.sprat-title span { font-weight: 500; font-size: 13px; color: #64748b; }

.sobe-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 16px; }
.soba-card { background: white; border-radius: 16px; padding: 16px; border: 1px solid #e2e8f0; display: flex; flex-direction: column; justify-content: space-between; min-height: 170px; }
.soba-card.slobodna { border-top: 4px solid #10b981; }
.soba-card.zauzeta { border-top: 4px solid #ef4444; }
.soba-card.čišćenje { border-top: 4px solid #f59e0b; }

.card-top { display: flex; justify-content: space-between; align-items: center; }
.tip-label { font-size: 10px; font-weight: 800; color: #64748b; text-transform: uppercase; background: #f1f5f9; padding: 2px 6px; border-radius: 4px; }
.bide-tag { color: #2563eb; margin-left: 2px; }
.status-pill { font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 12px; }
.status-pill.slobodna { background: #dcfce7; color: #15803d; }
.status-pill.zauzeta { background: #fee2e2; color: #b91c1c; }
.status-pill.čišćenje { background: #fef3c7; color: #b45309; }

.soba-header-row { display: flex; justify-content: space-between; align-items: center; margin-top: 6px; }
.soba-broj { font-size: 19px; font-weight: 800; }
.kapacitet-badge { font-size: 12px; font-weight: 700; background: #e2e8f0; color: #334155; padding: 2px 6px; border-radius: 6px; }

.gost-info { font-size: 13px; color: #64748b; margin-top: 2px; font-weight: 500; }

.card-action-btn { margin-top: 10px; }

.status-select { 
  width: 100%; 
  padding: 8px; 
  border-radius: 8px; 
  border: 1px solid #cbd5e1; 
  font-weight: 700; 
  cursor: pointer; 
  font-size: 13px;
  outline: none;
}
.status-select.slobodna { background: #dcfce7; color: #15803d; border-color: #86efac; }
.status-select.zauzeta { background: #fee2e2; color: #b91c1c; border-color: #fca5a5; }
.status-select.čišćenje { background: #fef3c7; color: #b45309; border-color: #fde047; }

/* =========================================================
   POTPUNA PRILAGODBA ZA MOBITELE (POPKATNO / OKOMITO)
   ========================================================= */
@media screen and (max-width: 768px) {
  .layout-container { 
    flex-direction: column !important; 
    width: 100vw !important; 
  }
  
  .sidebar { 
    width: 100% !important; 
    min-width: 100% !important; 
    padding: 12px 16px !important; 
    flex-direction: row !important; 
    justify-content: space-between !important; 
    align-items: center !important; 
    height: auto !important;
  }

  .brand { margin-bottom: 0 !important; }
  .brand-icon { font-size: 20px !important; padding: 6px !important; }
  .brand h2 { font-size: 16px !important; }
  .brand p { font-size: 10px !important; }

  .nav-menu, .system-status { display: none !important; }

  .main-content { 
    padding: 12px !important; 
    width: 100% !important; 
  }

  /* Statistika u 2 stupca sa zbijenim paddingom */
  .stats-grid { 
    grid-template-columns: repeat(2, 1fr) !important; 
    gap: 8px !important; 
    margin: 12px 0 !important; 
  }
  .stat-card { padding: 10px !important; gap: 8px !important; }
  .stat-value { font-size: 18px !important; }
  .stat-icon { font-size: 18px !important; padding: 6px !important; }

  /* Filteri se ljepše ređaju */
  .filter-section { padding: 10px !important; margin-bottom: 16px !important; }
  .filter-row { gap: 4px !important; }
  .filter-label { min-width: 100% !important; margin-top: 4px !important; margin-bottom: 2px !important; }
  .filter-chip { font-size: 11px !important; padding: 4px 8px !important; }

  /* Sobe u 2 prilagođene kolone na mobitelu */
  .sobe-grid { 
    grid-template-columns: repeat(2, 1fr) !important; 
    gap: 8px !important; 
  }
  .soba-card { padding: 10px !important; min-height: 140px !important; }
  .soba-broj { font-size: 15px !important; }
  .status-select { font-size: 11px !important; padding: 6px !important; }
}
</style>