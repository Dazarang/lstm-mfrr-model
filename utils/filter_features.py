#### ALL columns
def pick_region_filter(region, remove_balancing=False):
    """
    Returns a list of column names specific to the given region.

    Args:
        region (str): The region identifier (e.g., "SE1", "SE2", "SE3", "SE4", "SE").
        remove_balancing (bool): If True, removes balancing-related columns from the output.

    Returns:
        list: A list of column names for the specified region.

    Raises:
        ValueError: If the provided region is not valid.
    """
    # SE1 columns:
    se1_columns = [
        "CongestionManagement_Countertrading_FROM_SE1_ChangeInCrosszonalExchange(MW)",
        "Outages_UnavailabilityInTransmissionGrid_FROM_SE1_NewNTC",
        "Outages_UnavailabilityInTransmissionGrid_TO_SE1_NewNTC",
        "Load_ActualTotalLoad_SE1_TotalLoadValue",
        "Load_WeekAheadTotalLoadForecast_SE1_AvgMinMax",
        "Load_YearAheadTotalLoadForecast_SE1_AvgMinMax",
        "Load_MonthAheadTotalLoadForecast_SE1_AvgMinMax",
        "Load_DayAheadTotalLoadForecast_SE1_TotalLoadValue",
        "Balancing_ImbalancePrices_SE1_PositiveImbalancePrice",
        "Balancing_ImbalancePrices_SE1_NegativeImbalancePrice",
        "Balancing_AggregatedBalancingEnergyBids_SE1_mFRR_OfferedUpBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE1_mFRR_OfferedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE1_mFRR_ActivatedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE1_mFRR_ActivatedUpBidVolume[MW]",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE1_aFRR_Down_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE1_aFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE1_FCR_Symmetric_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE1_mFRR_Down_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE1_mFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE1_aFRR_Down_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE1_aFRR_Up_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE1_FCR_Symmetric_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE1_mFRR_Down_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE1_mFRR_Up_Price(MW/ISP)",
        "Balancing_PricesOfActivatedBalancingEnergy_SE1_aFRR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE1_FCR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE1_mFRR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE1_aFRR_NotSpecifiedDownPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE1_FCR_NotSpecifiedDownPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE1_mFRR_NotSpecifiedDownPrice",
        "Balancing_ActivatedBalancingEnergy_SE1_aFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE1_FCR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE1_mFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE1_aFRR_NotSpecifiedDownActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE1_FCR_NotSpecifiedDownActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE1_mFRR_NotSpecifiedDownActivatedVolume",
        "Balancing_AcceptedAggregatedOffers_SE1_aFRR_NotSpecifiedUpAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE1_mFRR_NotSpecifiedUpAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE1_aFRR_NotSpecifiedDownAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE1_mFRR_NotSpecifiedDownAcceptedVolume",
        "Transmission_ImplicitAllocationsNetPositions_SE1_Daily_Export_NetPosition[MW]",
        "Transmission_ImplicitAllocationsNetPositions_SE1_Daily_Import_NetPosition[MW]",
        "Transmission_ForecastedYearAheadTransferCapacities_TO_SE1_ForecastTransferCapacity",
        "Transmission_ForecastedYearAheadTransferCapacities_FROM_SE1_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_TO_SE1_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_FROM_SE1_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_TO_SE1_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_FROM_SE1_ForecastTransferCapacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_TO_SE1_Capacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_FROM_SE1_Capacity",
        "Transmission_PhysicalFlows_TO_SE1_FlowValue",
        "Transmission_PhysicalFlows_FROM_SE1_FlowValue",
        "Transmission_EnergyPrices_SE1_Price[Currency/MWh]",
        "Generation_CurrentGenerationForecastForWindAndSolar_SE1_AggregatedGenerationForecast",
        "Generation_AggregatedFillingRateOfWaterReservoirsAndHydroStoragePlants_SE1_StoredEnergy",
        "Generation_DayAheadAggregatedGeneration_SE1_ScheduledGeneration",
        "Generation_DayAheadGenerationForecastForWindAndSolar_SE1_AggregatedGenerationForecast",
        "Outages_UnavailabilityOfProductionUnits_SE1_HydroWaterReservoir_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE1_WindOnshore_UnavailableCapacity",
    ]

    # SE2 columns:
    se2_columns = [
        "CongestionManagement_Countertrading_FROM_SE2_ChangeInCrosszonalExchange(MW)",
        "CongestionManagement_Countertrading_TO_SE2_ChangeInCrosszonalExchange(MW)",
        "Outages_UnavailabilityInTransmissionGrid_FROM_SE2_NewNTC",
        "Outages_UnavailabilityInTransmissionGrid_TO_SE2_NewNTC",
        "Load_ActualTotalLoad_SE2_TotalLoadValue",
        "Load_WeekAheadTotalLoadForecast_SE2_AvgMinMax",
        "Load_YearAheadTotalLoadForecast_SE2_AvgMinMax",
        "Load_MonthAheadTotalLoadForecast_SE2_AvgMinMax",
        "Load_DayAheadTotalLoadForecast_SE2_TotalLoadValue",
        "Balancing_ImbalancePrices_SE2_PositiveImbalancePrice",
        "Balancing_ImbalancePrices_SE2_NegativeImbalancePrice",
        "Balancing_AggregatedBalancingEnergyBids_SE2_mFRR_OfferedUpBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE2_mFRR_OfferedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE2_mFRR_ActivatedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE2_mFRR_ActivatedUpBidVolume[MW]",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE2_aFRR_Down_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE2_aFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE2_FCR_Symmetric_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE2_mFRR_Down_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE2_mFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE2_aFRR_Down_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE2_aFRR_Up_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE2_FCR_Symmetric_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE2_mFRR_Down_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE2_mFRR_Up_Price(MW/ISP)",
        "Balancing_PricesOfActivatedBalancingEnergy_SE2_aFRR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE2_FCR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE2_mFRR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE2_aFRR_NotSpecifiedDownPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE2_FCR_NotSpecifiedDownPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE2_mFRR_NotSpecifiedDownPrice",
        "Balancing_ActivatedBalancingEnergy_SE2_aFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE2_FCR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE2_mFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE2_aFRR_NotSpecifiedDownActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE2_FCR_NotSpecifiedDownActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE2_mFRR_NotSpecifiedDownActivatedVolume",
        "Balancing_AcceptedAggregatedOffers_SE2_aFRR_NotSpecifiedUpAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE2_mFRR_NotSpecifiedUpAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE2_aFRR_NotSpecifiedDownAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE2_mFRR_NotSpecifiedDownAcceptedVolume",
        "Transmission_ImplicitAllocationsNetPositions_SE2_Daily_Export_NetPosition[MW]",
        "Transmission_ForecastedYearAheadTransferCapacities_TO_SE2_ForecastTransferCapacity",
        "Transmission_ForecastedYearAheadTransferCapacities_FROM_SE2_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_TO_SE2_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_FROM_SE2_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_TO_SE2_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_FROM_SE2_ForecastTransferCapacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_TO_SE2_Capacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_FROM_SE2_Capacity",
        "Transmission_PhysicalFlows_TO_SE2_FlowValue",
        "Transmission_PhysicalFlows_FROM_SE2_FlowValue",
        "Transmission_EnergyPrices_SE2_Price[Currency/MWh]",
        "Generation_CurrentGenerationForecastForWindAndSolar_SE2_AggregatedGenerationForecast",
        "Generation_AggregatedFillingRateOfWaterReservoirsAndHydroStoragePlants_SE2_StoredEnergy",
        "Generation_DayAheadAggregatedGeneration_SE2_ScheduledGeneration",
        "Generation_DayAheadGenerationForecastForWindAndSolar_SE2_AggregatedGenerationForecast",
        "Outages_UnavailabilityOfProductionUnits_SE2_HydroWaterReservoir_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE2_WindOnshore_UnavailableCapacity",
    ]

    # SE3 columns:
    se3_columns = [
        "CongestionManagement_Countertrading_FROM_SE3_ChangeInCrosszonalExchange(MW)",
        "CongestionManagement_Countertrading_TO_SE3_ChangeInCrosszonalExchange(MW)",
        "Outages_UnavailabilityInTransmissionGrid_FROM_SE3_NewNTC",
        "Outages_UnavailabilityInTransmissionGrid_TO_SE3_NewNTC",
        "Load_ActualTotalLoad_SE3_TotalLoadValue",
        "Load_WeekAheadTotalLoadForecast_SE3_AvgMinMax",
        "Load_YearAheadTotalLoadForecast_SE3_AvgMinMax",
        "Load_MonthAheadTotalLoadForecast_SE3_AvgMinMax",
        "Load_DayAheadTotalLoadForecast_SE3_TotalLoadValue",
        "Balancing_ImbalancePrices_SE3_PositiveImbalancePrice",
        "Balancing_ImbalancePrices_SE3_NegativeImbalancePrice",
        "Balancing_AggregatedBalancingEnergyBids_SE3_mFRR_OfferedUpBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE3_mFRR_OfferedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE3_mFRR_ActivatedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE3_mFRR_ActivatedUpBidVolume[MW]",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE3_aFRR_Down_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE3_aFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE3_FCR_Symmetric_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE3_mFRR_Down_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE3_mFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE3_aFRR_Down_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE3_aFRR_Up_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE3_FCR_Symmetric_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE3_mFRR_Down_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE3_mFRR_Up_Price(MW/ISP)",
        "Balancing_PricesOfActivatedBalancingEnergy_SE3_aFRR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE3_FCR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE3_mFRR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE3_aFRR_NotSpecifiedDownPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE3_FCR_NotSpecifiedDownPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE3_mFRR_NotSpecifiedDownPrice",
        "Balancing_ActivatedBalancingEnergy_SE3_aFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE3_FCR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE3_mFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE3_aFRR_NotSpecifiedDownActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE3_FCR_NotSpecifiedDownActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE3_mFRR_NotSpecifiedDownActivatedVolume",
        "Balancing_AcceptedAggregatedOffers_SE3_aFRR_NotSpecifiedUpAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE3_mFRR_NotSpecifiedUpAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE3_aFRR_NotSpecifiedDownAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE3_mFRR_NotSpecifiedDownAcceptedVolume",
        "Transmission_ImplicitAllocationsNetPositions_SE3_Daily_Export_NetPosition[MW]",
        "Transmission_ImplicitAllocationsNetPositions_SE3_Daily_Import_NetPosition[MW]",
        "Transmission_ForecastedYearAheadTransferCapacities_TO_SE3_ForecastTransferCapacity",
        "Transmission_ForecastedYearAheadTransferCapacities_FROM_SE3_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_TO_SE3_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_FROM_SE3_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_TO_SE3_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_FROM_SE3_ForecastTransferCapacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_TO_SE3_Capacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_FROM_SE3_Capacity",
        "Transmission_PhysicalFlows_TO_SE3_FlowValue",
        "Transmission_PhysicalFlows_FROM_SE3_FlowValue",
        "Transmission_EnergyPrices_SE3_Price[Currency/MWh]",
        "Generation_CurrentGenerationForecastForWindAndSolar_SE3_AggregatedGenerationForecast",
        "Generation_AggregatedFillingRateOfWaterReservoirsAndHydroStoragePlants_SE3_StoredEnergy",
        "Generation_DayAheadAggregatedGeneration_SE3_ScheduledGeneration",
        "Generation_DayAheadGenerationForecastForWindAndSolar_SE3_AggregatedGenerationForecast",
        "Outages_UnavailabilityOfProductionUnits_SE3_HydroWaterReservoir_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE3_WindOnshore_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE3_Fossil Gas_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE3_FossilOil_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE3_Nuclear_UnavailableCapacity",
    ]

    # SE4 columns:
    se4_columns = [
        "CongestionManagement_Countertrading_FROM_SE4_ChangeInCrosszonalExchange(MW)",
        "Outages_UnavailabilityInTransmissionGrid_FROM_SE4_NewNTC",
        "Outages_UnavailabilityInTransmissionGrid_TO_SE4_NewNTC",
        "Load_ActualTotalLoad_SE4_TotalLoadValue",
        "Load_WeekAheadTotalLoadForecast_SE4_AvgMinMax",
        "Load_YearAheadTotalLoadForecast_SE4_AvgMinMax",
        "Load_MonthAheadTotalLoadForecast_SE4_AvgMinMax",
        "Load_DayAheadTotalLoadForecast_SE4_TotalLoadValue",
        "Balancing_ImbalancePrices_SE4_PositiveImbalancePrice",
        "Balancing_ImbalancePrices_SE4_NegativeImbalancePrice",
        "Balancing_AggregatedBalancingEnergyBids_SE4_mFRR_OfferedUpBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE4_mFRR_OfferedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE4_mFRR_ActivatedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_SE4_mFRR_ActivatedUpBidVolume[MW]",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE4_aFRR_Down_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE4_aFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE4_FCR_Symmetric_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE4_mFRR_Down_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE4_mFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE4_aFRR_Down_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE4_aFRR_Up_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE4_FCR_Symmetric_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE4_mFRR_Down_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE4_mFRR_Up_Price(MW/ISP)",
        "Balancing_PricesOfActivatedBalancingEnergy_SE4_aFRR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE4_FCR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE4_mFRR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE4_aFRR_NotSpecifiedDownPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE4_FCR_NotSpecifiedDownPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_SE4_mFRR_NotSpecifiedDownPrice",
        "Balancing_ActivatedBalancingEnergy_SE4_aFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE4_FCR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE4_mFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE4_aFRR_NotSpecifiedDownActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE4_FCR_NotSpecifiedDownActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE4_mFRR_NotSpecifiedDownActivatedVolume",
        "Balancing_AcceptedAggregatedOffers_SE4_aFRR_NotSpecifiedUpAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE4_mFRR_NotSpecifiedUpAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE4_aFRR_NotSpecifiedDownAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_SE4_mFRR_NotSpecifiedDownAcceptedVolume",
        "Transmission_ImplicitAllocationsNetPositions_SE4_Daily_Export_NetPosition[MW]",
        "Transmission_ImplicitAllocationsNetPositions_SE4_Daily_Import_NetPosition[MW]",
        "Transmission_ForecastedYearAheadTransferCapacities_TO_SE4_ForecastTransferCapacity",
        "Transmission_ForecastedYearAheadTransferCapacities_FROM_SE4_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_TO_SE4_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_FROM_SE4_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_TO_SE4_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_FROM_SE4_ForecastTransferCapacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_TO_SE4_Capacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_FROM_SE4_Capacity",
        "Transmission_PhysicalFlows_TO_SE4_FlowValue",
        "Transmission_PhysicalFlows_FROM_SE4_FlowValue",
        "Transmission_EnergyPrices_SE4_Price[Currency/MWh]",
        "Generation_CurrentGenerationForecastForWindAndSolar_SE4_AggregatedGenerationForecast",
        "Generation_AggregatedFillingRateOfWaterReservoirsAndHydroStoragePlants_SE4_StoredEnergy",
        "Generation_DayAheadAggregatedGeneration_SE4_ScheduledGeneration",
        "Generation_DayAheadGenerationForecastForWindAndSolar_SE4_AggregatedGenerationForecast",
        "Outages_UnavailabilityOfProductionUnits_SE4_WindOnshore_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE4_Fossil Gas_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE4_FossilOil_UnavailableCapacity",
    ]

    # SE columns:
    se_columns = [
        "Outages_UnavailabilityInTransmissionGrid_FROM_SE_NewNTC",
        "Outages_UnavailabilityInTransmissionGrid_TO_SE_NewNTC",
        "Load_ActualTotalLoad_SE_TotalLoadValue",
        "Load_WeekAheadTotalLoadForecast_SE_AvgMinMax",
        "Load_YearAheadTotalLoadForecast_SE_AvgMinMax",
        "Load_MonthAheadTotalLoadForecast_SE_AvgMinMax",
        "Load_DayAheadTotalLoadForecast_SE_TotalLoadValue",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE_aFRR_Down_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE_aFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE_FCR_Symmetric_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_SE_FCR_Symmetric_Price(MW/ISP)",
        "Balancing_ActivatedBalancingEnergy_SE_aFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_SE_aFRR_NotSpecifiedDownActivatedVolume",
        "Transmission_ForecastedYearAheadTransferCapacities_TO_SE_ForecastTransferCapacity",
        "Transmission_ForecastedYearAheadTransferCapacities_FROM_SE_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_TO_SE_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_FROM_SE_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_TO_SE_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_FROM_SE_ForecastTransferCapacity",
        "Transmission_PhysicalFlows_TO_SE_FlowValue",
        "Transmission_PhysicalFlows_FROM_SE_FlowValue",
        "Generation_CurrentGenerationForecastForWindAndSolar_SE_AggregatedGenerationForecast",
        "Generation_AggregatedFillingRateOfWaterReservoirsAndHydroStoragePlants_SE_StoredEnergy",
        "Generation_DayAheadAggregatedGeneration_SE_ScheduledGeneration",
        "Generation_DayAheadGenerationForecastForWindAndSolar_SE_AggregatedGenerationForecast",
        "Outages_UnavailabilityOfProductionUnits_SE_HydroWaterReservoir_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE_WindOnshore_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE_Fossil Gas_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE_FossilOil_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_SE_Nuclear_UnavailableCapacity",
    ]

    if region == "SE1":
        selected_columns = se1_columns
    elif region == "SE2":
        selected_columns = se2_columns
    elif region == "SE3":
        selected_columns = se3_columns
    elif region == "SE4":
        selected_columns = se4_columns
    elif region == "SE":
        selected_columns = se_columns
    else:
        raise ValueError(f"Invalid region provided: {region}. Must be one of SE1, SE2, SE3, SE4, SE.")

    if remove_balancing:
        balancing_patterns = [
            "Balancing_ImbalancePrices_*region*_PositiveImbalancePrice",
            "Balancing_ImbalancePrices_*region*_NegativeImbalancePrice",
            "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_OfferedUpBidVolume[MW]",
            "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_OfferedDownBidVolume[MW]",
            "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_ActivatedDownBidVolume[MW]",
            "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_ActivatedUpBidVolume[MW]",
            "Balancing_PricesOfActivatedBalancingEnergy_*region*_aFRR_NotSpecifiedUpPrice",
            "Balancing_PricesOfActivatedBalancingEnergy_*region*_FCR_NotSpecifiedUpPrice",
            "Balancing_PricesOfActivatedBalancingEnergy_*region*_aFRR_NotSpecifiedDownPrice",
            "Balancing_PricesOfActivatedBalancingEnergy_*region*_FCR_NotSpecifiedDownPrice",
            "Balancing_ActivatedBalancingEnergy_*region*_aFRR_NotSpecifiedUpActivatedVolume",
            "Balancing_ActivatedBalancingEnergy_*region*_FCR_NotSpecifiedUpActivatedVolume",
            "Balancing_ActivatedBalancingEnergy_*region*_aFRR_NotSpecifiedDownActivatedVolume",
            "Balancing_ActivatedBalancingEnergy_*region*_FCR_NotSpecifiedDownActivatedVolume",
            "Balancing_AcceptedAggregatedOffers_*region*_aFRR_NotSpecifiedUpAcceptedVolume",
            "Balancing_AcceptedAggregatedOffers_*region*_mFRR_NotSpecifiedUpAcceptedVolume",
            "Balancing_AcceptedAggregatedOffers_*region*_aFRR_NotSpecifiedDownAcceptedVolume",
            "Balancing_AcceptedAggregatedOffers_*region*_mFRR_NotSpecifiedDownAcceptedVolume",
            # "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpPrice",
            # "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedDownPrice",
            # "Balancing_ActivatedBalancingEnergy_SE3_mFRR_NotSpecifiedUpActivatedVolume",
            # "Balancing_ActivatedBalancingEnergy_SE3_mFRR_NotSpecifiedDownActivatedVolume"
        ]
        # Replace *region* with the actual region
        balancing_patterns = [pattern.replace("*region*", region) for pattern in balancing_patterns]
        selected_columns = [col for col in selected_columns if not any(pattern in col for pattern in balancing_patterns)]

    return selected_columns


# Filtering
def create_region_filter(filter_number, region, remove_balancing=False):
    """
    Creates a region-specific filter list based on the selected filter number and user region.

    Args:
        filter_number (int): The filter number to use (1, 2, 3, 4 or 5)
        region (str): The region name to replace "*region*" with
        remove_balancing (bool): If True, removes balancing-related columns from the output.

    Returns:
        list: The selected filter list with "*region*" replaced by the region
    """

    # 1. filter no afrr/fcr
    region_filter_1 = [
        "CongestionManagement_Countertrading_FROM_*region*_ChangeInCrosszonalExchange(MW)",
        "CongestionManagement_Countertrading_TO_*region*_ChangeInCrosszonalExchange(MW)",
        "Outages_UnavailabilityOfProductionUnits_*region*_HydroWaterReservoir_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_WindOnshore_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_Fossil Gas_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_FossilOil_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_Nuclear_UnavailableCapacity",
        "Outages_UnavailabilityInTransmissionGrid_FROM_*region*_NewNTC",
        "Outages_UnavailabilityInTransmissionGrid_TO_*region*_NewNTC",
        "Load_ActualTotalLoad_*region*_TotalLoadValue",
        "Load_WeekAheadTotalLoadForecast_*region*_AvgMinMax",
        "Load_YearAheadTotalLoadForecast_*region*_AvgMinMax",
        "Load_MonthAheadTotalLoadForecast_*region*_AvgMinMax",
        "Load_DayAheadTotalLoadForecast_*region*_TotalLoadValue",
        "Balancing_ImbalancePrices_*region*_PositiveImbalancePrice",
        "Balancing_ImbalancePrices_*region*_NegativeImbalancePrice",
        "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_OfferedUpBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_OfferedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_ActivatedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_ActivatedUpBidVolume[MW]",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_*region*_mFRR_Down_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_*region*_mFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_*region*_mFRR_Down_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_*region*_mFRR_Up_Price(MW/ISP)",
        "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedDownPrice",
        "Balancing_ActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedDownActivatedVolume",
        "Balancing_AcceptedAggregatedOffers_*region*_mFRR_NotSpecifiedUpAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_*region*_mFRR_NotSpecifiedDownAcceptedVolume",
        "Transmission_ImplicitAllocationsNetPositions_*region*_Daily_Export_NetPosition[MW]",
        "Transmission_ImplicitAllocationsNetPositions_*region*_Daily_Import_NetPosition[MW]",
        "Transmission_ForecastedYearAheadTransferCapacities_TO_*region*_ForecastTransferCapacity",
        "Transmission_ForecastedYearAheadTransferCapacities_FROM_*region*_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_TO_*region*_ForecastTransferCapacity",
        "Transmission_ForecastedMonthAheadTransferCapacities_FROM_*region*_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_TO_*region*_ForecastTransferCapacity",
        "Transmission_ForecastedWeekAheadTransferCapacities_FROM_*region*_ForecastTransferCapacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_TO_*region*_Capacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_FROM_*region*_Capacity",
        "Transmission_PhysicalFlows_TO_*region*_FlowValue",
        "Transmission_PhysicalFlows_FROM_*region*_FlowValue",
        "Transmission_EnergyPrices_*region*_Price[Currency/MWh]",
        "Generation_CurrentGenerationForecastForWindAndSolar_*region*_AggregatedGenerationForecast",
        "Generation_AggregatedFillingRateOfWaterReservoirsAndHydroStoragePlants_*region*_StoredEnergy",
        "Generation_DayAheadAggregatedGeneration_*region*_ScheduledGeneration",
        "Generation_DayAheadGenerationForecastForWindAndSolar_*region*_AggregatedGenerationForecast",
    ]

    # 2. filter no afrr/fcr, no forecast
    region_filter_2 = [
        "CongestionManagement_Countertrading_FROM_*region*_ChangeInCrosszonalExchange(MW)",
        "CongestionManagement_Countertrading_TO_*region*_ChangeInCrosszonalExchange(MW)",
        "Outages_UnavailabilityOfProductionUnits_*region*_HydroWaterReservoir_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_WindOnshore_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_Fossil Gas_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_FossilOil_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_Nuclear_UnavailableCapacity",
        "Outages_UnavailabilityInTransmissionGrid_FROM_*region*_NewNTC",
        "Outages_UnavailabilityInTransmissionGrid_TO_*region*_NewNTC",
        "Load_ActualTotalLoad_*region*_TotalLoadValue",
        "Balancing_ImbalancePrices_*region*_PositiveImbalancePrice",
        "Balancing_ImbalancePrices_*region*_NegativeImbalancePrice",
        "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_OfferedUpBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_OfferedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_ActivatedDownBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_ActivatedUpBidVolume[MW]",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_*region*_mFRR_Down_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_*region*_mFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_*region*_mFRR_Down_Price(MW/ISP)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_*region*_mFRR_Up_Price(MW/ISP)",
        "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedDownPrice",
        "Balancing_ActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedDownActivatedVolume",
        "Balancing_AcceptedAggregatedOffers_*region*_mFRR_NotSpecifiedUpAcceptedVolume",
        "Balancing_AcceptedAggregatedOffers_*region*_mFRR_NotSpecifiedDownAcceptedVolume",
        "Transmission_ImplicitAllocationsNetPositions_*region*_Daily_Export_NetPosition[MW]",
        "Transmission_ImplicitAllocationsNetPositions_*region*_Daily_Import_NetPosition[MW]",
        "Transmission_OfferedIntradayTransferCapacityImplicit_TO_*region*_Capacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_FROM_*region*_Capacity",
        "Transmission_PhysicalFlows_TO_*region*_FlowValue",
        "Transmission_PhysicalFlows_FROM_*region*_FlowValue",
        "Transmission_EnergyPrices_*region*_Price[Currency/MWh]",
        "Generation_AggregatedFillingRateOfWaterReservoirsAndHydroStoragePlants_*region*_StoredEnergy",
        "Generation_DayAheadAggregatedGeneration_*region*_ScheduledGeneration",
    ]
    # 5. filter no afrr/fcr, no forecast
    region_filter_5 = [
        "CongestionManagement_Countertrading_FROM_*region*_ChangeInCrosszonalExchange(MW)",
        "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpPrice",
        "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedDownPrice",
        "CongestionManagement_Countertrading_TO_*region*_ChangeInCrosszonalExchange(MW)",
        "Outages_UnavailabilityOfProductionUnits_*region*_HydroWaterReservoir_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_WindOnshore_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_Fossil Gas_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_FossilOil_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_Nuclear_UnavailableCapacity",
        "Outages_UnavailabilityInTransmissionGrid_FROM_*region*_NewNTC",
        "Outages_UnavailabilityInTransmissionGrid_TO_*region*_NewNTC",
        "Load_ActualTotalLoad_*region*_TotalLoadValue",
        "Balancing_ActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_ActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedDownActivatedVolume",
        "Transmission_ImplicitAllocationsNetPositions_*region*_Daily_Export_NetPosition[MW]",
        "Transmission_ImplicitAllocationsNetPositions_*region*_Daily_Import_NetPosition[MW]",
        "Transmission_OfferedIntradayTransferCapacityImplicit_TO_*region*_Capacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_FROM_*region*_Capacity",
        "Transmission_PhysicalFlows_TO_*region*_FlowValue",
        "Transmission_PhysicalFlows_FROM_*region*_FlowValue",
        "Generation_AggregatedFillingRateOfWaterReservoirsAndHydroStoragePlants_*region*_StoredEnergy",
        "Generation_DayAheadAggregatedGeneration_*region*_ScheduledGeneration",
    ]

    # 3. filter no afrr/fcr, no forecast, no down
    region_filter_3 = [
        "CongestionManagement_Countertrading_FROM_*region*_ChangeInCrosszonalExchange(MW)",
        "CongestionManagement_Countertrading_TO_*region*_ChangeInCrosszonalExchange(MW)",
        "Outages_UnavailabilityOfProductionUnits_*region*_HydroWaterReservoir_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_WindOnshore_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_Fossil Gas_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_FossilOil_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_Nuclear_UnavailableCapacity",
        "Outages_UnavailabilityInTransmissionGrid_FROM_*region*_NewNTC",
        "Outages_UnavailabilityInTransmissionGrid_TO_*region*_NewNTC",
        "Load_ActualTotalLoad_*region*_TotalLoadValue",
        "Balancing_ImbalancePrices_*region*_PositiveImbalancePrice",
        "Balancing_ImbalancePrices_*region*_NegativeImbalancePrice",
        "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_OfferedUpBidVolume[MW]",
        "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_ActivatedUpBidVolume[MW]",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_*region*_mFRR_Up_Volume(MW)",
        "Balancing_AmountAndPricesPaidOfBalancingReservesUnderContract_*region*_mFRR_Up_Price(MW/ISP)",
        "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpPrice",
        "Balancing_ActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpActivatedVolume",
        "Balancing_AcceptedAggregatedOffers_*region*_mFRR_NotSpecifiedUpAcceptedVolume",
        "Transmission_ImplicitAllocationsNetPositions_*region*_Daily_Export_NetPosition[MW]",
        "Transmission_ImplicitAllocationsNetPositions_*region*_Daily_Import_NetPosition[MW]",
        "Transmission_OfferedIntradayTransferCapacityImplicit_TO_*region*_Capacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_FROM_*region*_Capacity",
        "Transmission_PhysicalFlows_TO_*region*_FlowValue",
        "Transmission_PhysicalFlows_FROM_*region*_FlowValue",
        "Transmission_EnergyPrices_*region*_Price[Currency/MWh]",
        "Generation_AggregatedFillingRateOfWaterReservoirsAndHydroStoragePlants_*region*_StoredEnergy",
        "Generation_DayAheadAggregatedGeneration_*region*_ScheduledGeneration",
    ]

    # 4. filter no afrr/fcr, no forecast, no down, and some extras
    region_filter_4 = [
        "CongestionManagement_Countertrading_FROM_*region*_ChangeInCrosszonalExchange(MW)",
        "CongestionManagement_Countertrading_TO_*region*_ChangeInCrosszonalExchange(MW)",
        "Outages_UnavailabilityOfProductionUnits_*region*_HydroWaterReservoir_UnavailableCapacity",
        "Outages_UnavailabilityOfProductionUnits_*region*_WindOnshore_UnavailableCapacity",
        "Outages_UnavailabilityInTransmissionGrid_FROM_*region*_NewNTC",
        "Outages_UnavailabilityInTransmissionGrid_TO_*region*_NewNTC",
        "Load_ActualTotalLoad_*region*_TotalLoadValue",
        "Balancing_ImbalancePrices_*region*_PositiveImbalancePrice",
        "Balancing_ImbalancePrices_*region*_NegativeImbalancePrice",
        "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpPrice",
        "Balancing_ActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpActivatedVolume",
        "Transmission_OfferedIntradayTransferCapacityImplicit_TO_*region*_Capacity",
        "Transmission_OfferedIntradayTransferCapacityImplicit_FROM_*region*_Capacity",
        "Transmission_PhysicalFlows_TO_*region*_FlowValue",
        "Transmission_PhysicalFlows_FROM_*region*_FlowValue",
        "Transmission_EnergyPrices_*region*_Price[Currency/MWh]",
        "Generation_AggregatedFillingRateOfWaterReservoirsAndHydroStoragePlants_*region*_StoredEnergy",
        "Generation_DayAheadAggregatedGeneration_*region*_ScheduledGeneration",
    ]

    # Select the appropriate filter list based on the filter_number
    if filter_number == 1:
        selected_filter = region_filter_1
    elif filter_number == 2:
        selected_filter = region_filter_2
    elif filter_number == 3:
        selected_filter = region_filter_3
    elif filter_number == 4:
        selected_filter = region_filter_4
    elif filter_number == 5:
        selected_filter = region_filter_5
    else:
        raise ValueError("Filter number must be 1, 2, 3, 4 or 5")

    # Replace "*region*" with the user-specified region in each item
    region_filter = [item.replace("*region*", region) for item in selected_filter]

    if remove_balancing:
        balancing_patterns = [
            "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_OfferedUpBidVolume[MW]",
            "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_OfferedDownBidVolume[MW]",
            "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_ActivatedDownBidVolume[MW]",
            "Balancing_AggregatedBalancingEnergyBids_*region*_mFRR_ActivatedUpBidVolume[MW]",
            "Balancing_PricesOfActivatedBalancingEnergy_*region*_aFRR_NotSpecifiedUpPrice",
            "Balancing_PricesOfActivatedBalancingEnergy_*region*_FCR_NotSpecifiedUpPrice",
            "Balancing_PricesOfActivatedBalancingEnergy_*region*_aFRR_NotSpecifiedDownPrice",
            "Balancing_PricesOfActivatedBalancingEnergy_*region*_FCR_NotSpecifiedDownPrice",
            "Balancing_ActivatedBalancingEnergy_*region*_aFRR_NotSpecifiedUpActivatedVolume",
            "Balancing_ActivatedBalancingEnergy_*region*_FCR_NotSpecifiedUpActivatedVolume",
            "Balancing_ActivatedBalancingEnergy_*region*_aFRR_NotSpecifiedDownActivatedVolume",
            "Balancing_ActivatedBalancingEnergy_*region*_FCR_NotSpecifiedDownActivatedVolume",
            "Balancing_AcceptedAggregatedOffers_*region*_aFRR_NotSpecifiedUpAcceptedVolume",
            "Balancing_AcceptedAggregatedOffers_*region*_mFRR_NotSpecifiedUpAcceptedVolume",
            "Balancing_AcceptedAggregatedOffers_*region*_aFRR_NotSpecifiedDownAcceptedVolume",
            "Balancing_AcceptedAggregatedOffers_*region*_mFRR_NotSpecifiedDownAcceptedVolume",
            # "Balancing_ImbalancePrices_*region*_PositiveImbalancePrice",
            # "Balancing_ImbalancePrices_*region*_NegativeImbalancePrice",
            # "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedUpPrice",
            # "Balancing_PricesOfActivatedBalancingEnergy_*region*_mFRR_NotSpecifiedDownPrice",
            # "Balancing_ActivatedBalancingEnergy_SE3_mFRR_NotSpecifiedUpActivatedVolume",
            # "Balancing_ActivatedBalancingEnergy_SE3_mFRR_NotSpecifiedDownActivatedVolume"
        ]
        balancing_patterns = [pattern.replace("*region*", region) for pattern in balancing_patterns]
        region_filter = [col for col in region_filter if not any(pattern in col for pattern in balancing_patterns)]

    return region_filter
