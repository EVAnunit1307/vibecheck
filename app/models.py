from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Plan(Base):
    __tablename__ = "plans"
    
    id = Column(Integer, primary_key=True, index=True)
    area = Column(String, nullable=False)
    vibe = Column(String, nullable=False)
    budget_per_person = Column(Float, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    status = Column(String, default="voting")  # voting or finalized
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    votes = relationship("Vote", back_populates="plan")
    itinerary_items = relationship("ItineraryItem", back_populates="plan")


class Option(Base): #stores functions options for the plan
    __tablename__ = "options"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # dinner, bar, activity, late_bite
    price_range = Column(Integer, nullable=False)  # 1-4 ($, $$, $$$, $$$$)
    vibe = Column(String, nullable=False)  # chill, upbeat, fancy, casual
    description = Column(String)
    
    # Relationships
    votes = relationship("Vote", back_populates="option")


class Vote(Base):
    __tablename__ = "votes"
    
    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=False)
    option_id = Column(Integer, ForeignKey("options.id"), nullable=False)
    voter_id = Column(String, nullable=False)  # simple string ID, no accounts
    vote_type = Column(Boolean, nullable=False)  # True = thumbs up, False = thumbs down
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    plan = relationship("Plan", back_populates="votes")
    option = relationship("Option", back_populates="votes")


class ItineraryItem(Base): #final itinerary items for the plan
    __tablename__ = "itinerary_items"
    
    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("plans.id"), nullable=False)
    option_id = Column(Integer, ForeignKey("options.id"), nullable=False)
    order = Column(Integer, nullable=False)  # 1st stop, 2nd stop, etc.
    estimated_cost = Column(Float)
    
    # Relationships
    plan = relationship("Plan", back_populates="itinerary_items")