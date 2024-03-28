from dataclasses import dataclass, field


@dataclass
class InfoData:
    # /cgi/info.js data
    device_description: str | None = None
    display_serial: str | None = None
    sw_id_ems: int | None = None
    hw_id_ems: int | None = None
    countrycode: int | None = None
    sw_version_ems: str | None = None
    anz_charger: int | None = None
    soll_charger: int | None = None
    serial_emeter: str | None = None
    mac_emeter: str | None = None
    sw_version_emeter: str | None = None
    bl_version_emeter: str | None = None
    hw_id_emeter: int | None = None
    serial_wr: str | None = None
    mac_wr: int | None = None
    sw_id_wr: int | None = None
    hw_id_wr: int | None = None
    sw_version_wr: str | None = None
    bl_version_wr: str | None = None
    serial_ens: str | None = None
    mac_ens: int | None = None
    sw_id_ens: int | None = None
    hw_id_ens: int | None = None
    sw_version_ens: str | None = None
    bl_version_ens: str | None = None
    charger_serial: list[str] = field(default_factory=list)
    charger_mac: list[str] = field(default_factory=list)
    sw_id_charger: list[int] = field(default_factory=list)
    hw_id_charger: list[int] = field(default_factory=list)
    sw_version_charger: list[str] = field(default_factory=list)
    bl_version_charger: list[str] = field(default_factory=list)
    p_ems_max: int | None = None
    p_ems_maxdisc: int | None = None
    battery_sw: list[str] = field(default_factory=list)
    battery_hw: list[str] = field(default_factory=list)
    battery_serial: list[str] = field(default_factory=list)
    bm_update: list[str] = field(default_factory=list)
    bm_update_sw: list[str] = field(default_factory=list)
    bm_production: list[str] = field(default_factory=list)
    lg_battery_serial: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, info: dict) -> "InfoData":
        return cls(
            device_description=info.get("Device_Description"),
            display_serial=info.get("Display_Serial"),
            sw_id_ems=info.get("SW_ID_EMS"),
            hw_id_ems=info.get("HW_ID_EMS"),
            countrycode=info.get("countrycode"),
            sw_version_ems=info.get("SW_Version_EMS"),
            anz_charger=info.get("Anz_Charger"),
            soll_charger=info.get("Soll_Charger"),
            serial_emeter=info.get("Serial_EMeter"),
            mac_emeter=info.get("MAC_EMeter"),
            sw_version_emeter=info.get("SW_Version_EMeter"),
            bl_version_emeter=info.get("BL_Version_EMeter"),
            hw_id_emeter=info.get("HW_ID_EMeter"),
            serial_wr=info.get("Serial_WR"),
            mac_wr=info.get("MAC_WR"),
            sw_id_wr=info.get("SW_ID_WR"),
            hw_id_wr=info.get("HW_ID_WR"),
            sw_version_wr=info.get("SW_Version_WR"),
            bl_version_wr=info.get("BL_Version_WR"),
            serial_ens=info.get("Serial_ENS"),
            mac_ens=info.get("MAC_ENS"),
            sw_id_ens=info.get("SW_ID_ENS"),
            hw_id_ens=info.get("HW_ID_ENS"),
            sw_version_ens=info.get("SW_Version_ENS"),
            bl_version_ens=info.get("BL_Version_ENS"),
            charger_serial=info.get("Charger_Serial", []),
            charger_mac=info.get("Charger_MAC", []),
            sw_id_charger=info.get("SW_ID_Charger", []),
            hw_id_charger=info.get("HW_ID_Charger", []),
            sw_version_charger=info.get("SW_Version_Charger", []),
            bl_version_charger=info.get("BL_Version_Charger", []),
            p_ems_max=info.get("P_EMS_Max"),
            p_ems_maxdisc=info.get("P_EMS_MaxDisc"),
            battery_sw=info.get("BatterySW", []),
            battery_hw=info.get("BatteryHW", []),
            battery_serial=info.get("BatterySerial", []),
            bm_update=info.get("BM_Update", []),
            bm_update_sw=info.get("BM_UpdateSW", []),
            bm_production=info.get("BM_Production", []),
            lg_battery_serial=info.get("LG_Battery_Serial", []),
        )


@dataclass
class EnergyData:
    # /cgi/energy.js data
    total_grid_ac_dc: int | None = None  # Wh
    total_grid_dc_ac: int | None = None  # Wh
    total_inverter_ac_dc: int | None = None  # Wh
    total_inverter_dc_ac: int | None = None  # Wh
    total_charge_cycles: list[int] = field(default_factory=list)

    @classmethod
    def from_dict(cls, energy: dict) -> "EnergyData":
        return cls(
            total_grid_ac_dc=energy.get("EGrid_AC_DC"),
            total_grid_dc_ac=energy.get("EGrid_DC_AC"),
            total_inverter_ac_dc=energy.get("EWr_AC_DC"),
            total_inverter_dc_ac=energy.get("EWr_DC_AC"),
            total_charge_cycles=energy.get("Chrg_LoadCycles", []),
        )


@dataclass
class ServiceData:
    # /cgi/user_serv.js data
    hours_until_filter_maintenance: int | None = None  # Hours
    status_fan: int | None = None
    status_main: int | None = None

    @classmethod
    def from_dict(cls, service: dict) -> "ServiceData":
        return cls(
            hours_until_filter_maintenance=service.get("FilterZeit"),
            status_fan=service.get("Fan"),
            status_main=service.get("Main"),
        )


@dataclass
class WrData:
    nominal_power: int | None = None  # W
    u_verbund_l1: int | None = None  # V
    u_verbund_l2: int | None = None  # V
    u_verbund_l3: int | None = None  # V
    i_verbund_l1: int | None = None  # A
    i_verbund_l2: int | None = None  # A
    i_verbund_l3: int | None = None  # A
    u_insel_l1: int | None = None  # V
    u_insel_l2: int | None = None  # V
    u_insel_l3: int | None = None  # V
    i_insel_l1: int | None = None  # A
    i_insel_l2: int | None = None  # A
    i_insel_l3: int | None = None  # A
    temp_l1: int | None = None  # Celcius
    temp_l2: int | None = None  # Celcius
    temp_l3: int | None = None  # Celcius
    temp_board: int | None = None  # Celcius
    frequency_grid: int | None = None  # Hz
    online_status: int | None = None  # 0=Offline, 1=Online
    fan_speed: int | None = None  # percentage

    @classmethod
    def from_dict(cls, wr: dict) -> "WrData":
        return cls(
            nominal_power=wr.get("PSoll"),
            u_verbund_l1=wr.get("U Verbund L1"),
            u_verbund_l2=wr.get("U Verbund L2"),
            u_verbund_l3=wr.get("U Verbund L3"),
            i_verbund_l1=wr.get("I Verbund L1"),
            i_verbund_l2=wr.get("I Verbund L2"),
            i_verbund_l3=wr.get("I Verbund L3"),
            u_insel_l1=wr.get("U Insel L1"),
            u_insel_l2=wr.get("U Insel L2"),
            u_insel_l3=wr.get("U Insel L3"),
            i_insel_l1=wr.get("I Insel L1"),
            i_insel_l2=wr.get("I Insel L2"),
            i_insel_l3=wr.get("I Insel L3"),
            temp_l1=wr.get("Temp L1"),
            temp_l2=wr.get("Temp L2"),
            temp_l3=wr.get("Temp L3"),
            temp_board=wr.get("TBoard"),
            frequency_grid=wr.get("FNetz"),
            online_status=wr.get("OnlineStatus"),
            fan_speed=wr.get("Luefter"),
        )


@dataclass
class EMeterData:
    f_netz: int | None = None
    sens_state: int | None = None
    u_v_l1: int | None = None
    u_v_l2: int | None = None
    u_v_l3: int | None = None
    iw_v_l1: int | None = None
    iw_v_l2: int | None = None
    iw_v_l3: int | None = None
    ib_v_l1: int | None = None
    ib_v_l2: int | None = None
    ib_v_l3: int | None = None
    is_v_l1: int | None = None
    is_v_l2: int | None = None
    is_v_l3: int | None = None
    iw_pv_l1: int | None = None
    iw_pv_l2: int | None = None
    iw_pv_l3: int | None = None
    ib_pv_l1: int | None = None
    ib_pv_l2: int | None = None
    ib_pv_l3: int | None = None
    is_pv_l1: int | None = None
    is_pv_l2: int | None = None
    is_pv_l3: int | None = None

    @classmethod
    def from_dict(cls, emeter: dict) -> "EMeterData":
        return cls(
            f_netz=emeter.get("FNetz"),
            sens_state=emeter.get("SensState"),
            u_v_l1=emeter.get("U_V_L1"),
            u_v_l2=emeter.get("U_V_L2"),
            u_v_l3=emeter.get("U_V_L3"),
            iw_v_l1=emeter.get("Iw_V_L1"),
            iw_v_l2=emeter.get("Iw_V_L2"),
            iw_v_l3=emeter.get("Iw_V_L3"),
            ib_v_l1=emeter.get("Ib_V_L1"),
            ib_v_l2=emeter.get("Ib_V_L2"),
            ib_v_l3=emeter.get("Ib_V_L3"),
            is_v_l1=emeter.get("Is_V_L1"),
            is_v_l2=emeter.get("Is_V_L2"),
            is_v_l3=emeter.get("Is_V_L3"),
            iw_pv_l1=emeter.get("Iw_PV_L1"),
            iw_pv_l2=emeter.get("Iw_PV_L2"),
            iw_pv_l3=emeter.get("Iw_PV_L3"),
            ib_pv_l1=emeter.get("Ib_PV_L1"),
            ib_pv_l2=emeter.get("Ib_PV_L2"),
            ib_pv_l3=emeter.get("Ib_PV_L3"),
            is_pv_l1=emeter.get("Is_PV_L1"),
            is_pv_l2=emeter.get("Is_PV_L2"),
            is_pv_l3=emeter.get("Is_PV_L3"),
        )


@dataclass
class EnsData:
    f_netz: int | None = None
    u_v_l1: int | None = None
    u_v_l2: int | None = None
    u_v_l3: int | None = None

    @classmethod
    def from_dict(cls, ens: dict) -> "EnsData":
        return cls(
            f_netz=ens.get("FNetz"),
            u_v_l1=ens.get("U_V_L1"),
            u_v_l2=ens.get("U_V_L2"),
            u_v_l3=ens.get("U_V_L3"),
        )


@dataclass
class ChargerData:
    # TODO
    pass


@dataclass
class BattData:
    # TODO
    pass


@dataclass
class EmsData:
    # /cgi/ems_datajs data
    wr_data: WrData | None = None
    emeter_data: EMeterData | None = None
    ens_data: EnsData | None = None
    charger_data: ChargerData | None = None
    batt_data: BattData | None = None
